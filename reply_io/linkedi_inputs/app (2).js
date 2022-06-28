const puppeteer = require('puppeteer');
const { Pool } = require('pg');
const config = require('./config.json');
const path = require('path');

class db {

    constructor(config) {
        this.config = config;
        this.pool = new Pool(this.config);
    }

    async query(args) {
        let query = args.q,
            params = args.p;
        var res = await this.pool.query(query, params);
        return res.rows;
    }

    async update(args) {
        let query = args.q,
            params = args.p;
        var res = await this.pool.query(query, params);
        return res.rowCount;
    }

    async queryOne(args) {
        let query = args.q,
            params = args.p,
            data = null;
        var res = await this.pool.query(query, params);
        if (res.rows) {
            data = res.rows[0];
        }
        return data;
    }
}

class scrape {

    constructor(config) {
        this.config = config.sales;
        this.connDb = new db(config.db);
    }

    async launch() {
        this.browser = await puppeteer.launch({
            headless: false,
            executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
            ignoreDefaultArgs: ["--disable-extensions"],
            args: [
                '--start-maximized',
                //'--user-data-dir=C:/Users/kisho/AppData/Local/Google/Chrome/User Data/',
                //'--profile-directory=Default'
            ],
            defaultViewport: null,
            // slowMo: 250 
        });

        //const pages = await this.browser.pages();
        //this.currentTab = pages ? pages[0] : null;
        this.currentTab = await this.browser.newPage();
        this.currentTab.setDefaultTimeout(300000);
    }

    async login() {

        try {
            await this.currentTab.goto(this.config.login.url, { waitUntil: 'networkidle2' });

            const authenticationIframe = await this.currentTab.$('iframe');
            const authenticationIframeContent = await (authenticationIframe).contentFrame();

            await authenticationIframeContent.click(this.config.login.usernameSelector);
            await authenticationIframeContent.type(this.config.login.usernameSelector, this.config.login.username);

            await authenticationIframeContent.click(this.config.login.passwordSelector);
            await authenticationIframeContent.type(this.config.login.passwordSelector, this.config.login.password);

            await authenticationIframeContent.click(this.config.login.submitSelector);

            await this.currentTab.waitForResponse(response => response.status() === 200);

            const isError = await authenticationIframeContent.evaluate(() => {
                return document.querySelectorAll('#error-for-username', '#error-for-password').length;
            })

            if (isError) {
                return 'login-failed';
            }

            await this.currentTab.waitForNavigation();

            return 'login-success';

        } catch (err) {
            console.error(err);
            return 'login-error';
        }
    }

    async insertRecords(employeeInformationArr) {

        var insertValues = [],
            insertValuesStr = "";

        employeeInformationArr.forEach(emp => {
            insertValuesStr += "('" + emp.join("' , '") + "'), "
        });

        console.log(insertValuesStr);

        var insertInfoCnt = await this.connDb.query({ q: "INSERT mohit_table (col1, col2, col3, col4) $1 ", p: [insertValuesStr] });
    }


    async visitCompany(url) {

        await this.currentTab.waitForNavigation();
        await this.currentTab.goto(url, { waitUntil: 'networkidle2' });
        await this.currentTab.waitForSelector(this.config.company.allEmployeesSelector);
        await this.currentTab.click(this.config.company.allEmployeesSelector);
        await this.currentTab.waitForNavigation({ waitUntil: 'load' });
        await this.currentTab.click(this.config.company.jobSelector);

        for (var i = 0; i < this.config.company.jobFilters.length; i++) {
            var job = this.config.company.jobFilters[i];

            await this.currentTab.click(this.config.company.jobTextSelector);
            await this.currentTab.type(this.config.company.jobTextSelector, job, { delay: 400 });
            this.currentTab.keyboard.press('Enter');
            await this.currentTab.waitForTimeout(500);
            await this.currentTab.waitForResponse(response => response.status() === 200);
        }


        var employeeInformation = [];
        var doEmpScrape = true;

        while (doEmpScrape) {

            await this.currentTab.waitForTimeout(2000);
            await this.currentTab.waitForResponse(response => response.status() === 200);

            var isPaginationAvailable = await this.currentTab.evaluate((paginationSelector) => {
                return document.querySelectorAll(paginationSelector).length > 0;
            }, this.config.company.paginationSelector);

            if (!isPaginationAvailable) {
                doEmpScrape = false;
                break;
            }

            //await this.currentTab.waitForSelector(this.config.company.paginationSelector);

            for (var j = 0; j < 2; j++) {

                var paginationSelector = this.config.company.paginationSelector
                await this.currentTab.evaluate((paginationSelector) => {
                    let window = document.querySelector(paginationSelector);
                    window.scrollIntoView({
                        behavior: 'smooth',
                        block: 'end',
                        inline: "start"
                    });
                }, paginationSelector);

                await this.currentTab.waitForTimeout(1000);
                await this.currentTab.waitForResponse(response => response.status() === 200);

                var searchResultHoverableOutletSelector = this.config.company.searchResultHoverableOutletSelector;
                await this.currentTab.evaluate((searchResultHoverableOutletSelector) => {
                    let window = document.querySelector(searchResultHoverableOutletSelector);
                    window.scrollIntoView({
                        behavior: 'smooth',
                        block: 'end',
                        inline: "start"
                    });
                }, searchResultHoverableOutletSelector);

                await this.currentTab.waitForTimeout(1000);
                await this.currentTab.waitForResponse(response => response.status() === 200);
            }

            var employeeBatchInformation = await this.currentTab.evaluate((content, name, designation, company, location) =>
                Array.from(document.querySelectorAll(content)).map(compact => ({
                    Name: escape(compact.querySelector(name).innerText),
                    Designation: compact.querySelector(designation) && compact.querySelector(designation).innerText,
                    Company: compact.querySelector(company) && compact.querySelector(company).innerText,
                    Location: compact.querySelector(location) && compact.querySelector(location).innerText
                })), this.config.company.employeeSelector.content, this.config.company.employeeSelector.name, this.config.company.employeeSelector.designation, this.config.company.employeeSelector.company, this.config.company.employeeSelector.location)

            employeeInformation = employeeInformation.concat(employeeBatchInformation);

            var isPaginationNextSelectorDisabled = await this.currentTab.evaluate((paginationNextSelector) => {
                return document.querySelector(paginationNextSelector).disabled;
            }, this.config.company.paginationNextSelector);

            var isPaginationDisabled = await this.currentTab.evaluate((paginationDisabledSelector) => {
                return document.querySelectorAll(paginationDisabledSelector).length > 0;
            }, this.config.company.paginationDisabledSelector);

            if (isPaginationDisabled || isPaginationNextSelectorDisabled || employeeInformation.length >= this.config.company.employeeCountToScrape) {
                doEmpScrape = false;
            } else {
                await this.currentTab.click(this.config.company.paginationNextSelector);
                await this.currentTab.waitForTimeout(100);
                await this.currentTab.waitForResponse(response => response.status() === 200);
            }
        }

        return employeeInformation;
    }

    async sleep() {
        await new Promise((resolve, reject) => {
            setTimeout(function () {
                resolve(true);
            }, 300000)
        })
    }

    async exe() {



        var campaignQuery = "select * from campaign where scraper_status ='initializing' order by scraper_started_on ASC limit 1";
        var campaignRow = await this.connDb.queryOne({ "q": campaignQuery, "p": [] });

        if (campaignRow) {


            var companyQuery = `SELECT c.company_id,
                                c.campaign_id,
                                cmp.url AS name,
                                cmp.linkedin_url,
                                COUNT(cts.id) AS conts
                        FROM campaign_company c
                        JOIN company cmp ON cmp.id = c.company_id
                        LEFT JOIN contacts cts ON cts.company_id = cmp.id
                        WHERE c.campaign_id = $1
                        GROUP BY c.company_id,
                                c.campaign_id,
                                cmp.url,
                                cmp.linkedin_url
                        HAVING COUNT(cts.id) = 0`;

            var companyArr = await this.connDb.query({ "q": companyQuery, "p": [campaignRow.id] });
            if (companyArr && companyArr.length) {

            }

        } else {

            await this.sleep();

        }

        if (false) {
            await this.launch();
            var companies = ['https://www.linkedin.com/sales/company/2774359']
            let loginState = await this.login();
            console.log(loginState);

            while (companies.length) {
                var company = companies.shift();
                await this.visitCompany(company);
            }
        }
    }

}



(async () => {

    var pv = new scrape(config);
    var state = await pv.exe();

})()