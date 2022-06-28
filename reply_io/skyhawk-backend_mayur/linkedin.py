class linkedin():
    def __init__(self, config, webdriver):
        self.CONFIG = config
        self.DRIVER = webdriver

    def login(self):

        homeURL = self.CONFIG["login"]["home"]
        loginPath = self.CONFIG["login"]["path"]

        self.DRIVER.goto(homeURL, 'primary')
        currentUrl = self.DRIVER.getCurrentUrl()

        if loginPath in currentUrl:
            loginURL = self.CONFIG["login"]["url"]
            self.DRIVER.goto(loginURL, 'primary')

            loginConfig = self.CONFIG['login']
            username = loginConfig['username']
            usernameSelector = loginConfig['usernameSelector']
            password = loginConfig['password']
            passwordSelector = loginConfig['passwordSelector']
            iframeSelector = loginConfig['iframeSelector']

            logIfrmae = self.DRIVER.findElement(iframeSelector)
            self.DRIVER.switchToFrame(logIfrmae)

            usernameEle = self.DRIVER.findElement(usernameSelector)
            self.DRIVER.clear(usernameEle)

            passwordEle = self.DRIVER.findElement(passwordSelector)
            self.DRIVER.clear(passwordEle)

            self.DRIVER.sendKeys(usernameEle, username)
            self.DRIVER.sendKeys(passwordEle, password)

            self.DRIVER.submit(passwordEle)

            currentUrl = self.DRIVER.getCurrentUrl()
            if loginPath in currentUrl:
                return False
            else:
                return True
        else:
            return True

    def visitCompany(self, url):

        self.DRIVER.goto(url, 'primary')
        currentUrl = self.DRIVER.getCurrentUrl()
        allEmployeesSelector = self.CONFIG["company"]["allEmployeesSelector"]
        jobSelector = self.CONFIG["company"]["jobSelector"]
        jobFilters = self.CONFIG["company"]["jobFilters"]
        jobTextSelector = self.CONFIG["company"]["jobTextSelector"]
        paginationSelector = self.CONFIG["company"]["paginationSelector"]
        searchResultHoverableOutletSelector = self.CONFIG["company"]["searchResultHoverableOutletSelector"]

        contentSelector = self.CONFIG["company"]["employeeSelector"]["content"]
        nameSelector = self.CONFIG["company"]["employeeSelector"]["name"]
        designationSelector = self.CONFIG["company"]["employeeSelector"]["designation"]
        companySelector = self.CONFIG["company"]["employeeSelector"]["company"]
        locationSelector = self.CONFIG["company"]["employeeSelector"]["location"]

        allEmployeesEle = self.DRIVER.presenceOfElementLocated(
            allEmployeesSelector)
        self.DRIVER.click(allEmployeesEle)
        self.DRIVER.sleep(10)

        jobSelectorEle = self.DRIVER.presenceOfElementLocated(jobSelector)
        self.DRIVER.click(jobSelectorEle)
        self.DRIVER.sleep(10)
        jobTextSelectorEle = self.DRIVER.presenceOfElementLocated(
            jobTextSelector)
        self.DRIVER.click(jobTextSelectorEle)
        for jobtitle in jobFilters:
            self.DRIVER.sleep(5)
            self.DRIVER.sendKeys(jobTextSelectorEle, jobtitle, 0.5)
            self.DRIVER.enter(jobTextSelectorEle)
            self.DRIVER.sleep(3)

        employeeInformation = {}
        doEmpScrape = True

        while doEmpScrape:

            isPaginationAvailable = self.DRIVER.findElement(paginationSelector)

            if isPaginationAvailable:
                pass
            else:
                doEmpScrape = False

            for i in range(2):
                pageScrollScript = '''let window = document.querySelector('%s');
                    window.scrollIntoView({
                        behavior: 'smooth',
                        block: 'end',
                        inline: "start"
                    });''' % paginationSelector
                self.DRIVER.executeScript(pageScrollScript)

                self.DRIVER.sleep(10 / (i + 1))

                searchResultHoverableOutletScript = '''let window = document.querySelector('%s');
                    window.scrollIntoView({
                        behavior: 'smooth',
                        block: 'end',
                        inline: "start"
                    });''' % searchResultHoverableOutletSelector
                self.DRIVER.executeScript(searchResultHoverableOutletScript)

                self.DRIVER.sleep(10 / (i + 1))

            # employeeBatchInformationScript = """
            #     var __bl_content = '%s';
            #     var __bl_name = '%s';
            #     var __bl_designation = '%s';
            #     var __bl_company = '%s';
            #     var __bl_location = '%s';
            #     return Array.from(document.querySelectorAll(__bl_content)).map(compact => ({
            #         Name: escape(compact.querySelector(__bl_name).innerText),
            #         Designation: compact.querySelector(__bl_designation) && compact.querySelector(__bl_designation).innerText,
            #         Company: compact.querySelector(__bl_company) && compact.querySelector(__bl_company).innerText,
            #         Location: compact.querySelector(__bl_location) && compact.querySelector(__bl_location).innerText
            #     }));""" % (contentSelector, nameSelector, designationSelector, companySelector, locationSelector)

            employeeBatchInformationScript = """
                           var __bl_content = '%s';
                           var __bl_name = '%s';
                           var __bl_designation = '%s';
                           var __bl_company = '%s';
                           var __bl_location = '%s';
                           return Array.from(document.querySelectorAll(__bl_content)).map(compact => ({
                               Name: compact.querySelector(__bl_name).innerText,
                               Designation: compact.querySelector(__bl_designation) && compact.querySelector(__bl_designation).innerText,
                               Company: compact.querySelector(__bl_company) && compact.querySelector(__bl_company).innerText,
                               Location: compact.querySelector(__bl_location) && compact.querySelector(__bl_location).innerText
                           }));""" % (
            contentSelector, nameSelector, designationSelector, companySelector, locationSelector)

            employeeBatchInformation = self.DRIVER.executeScript(employeeBatchInformationScript)

            # print(employeeBatchInformation)



            print("intentional break");


            break

        return employeeBatchInformation
