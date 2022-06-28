import time
import pandas as pd

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
        companyWebsiteUrlSelector = self.CONFIG["company"]["companyWebsiteUrlSelector"]
        totalEmployeeCountToScrape = self.CONFIG["company"]["employeeCountToScrape"]
        jobSelector = self.CONFIG["company"]["jobSelector"]
        jobFilters = self.CONFIG["company"]["jobFilters1"]
        jobLevles = self.CONFIG["company"]["jobLevles"]
        jobTextSelector = self.CONFIG["company"]["jobTextSelector"]
        jobTitleRemoveSelector = self.CONFIG["company"]["jobTitleRemoveSelector"]
        paginationSelector = self.CONFIG["company"]["paginationSelector"]
        paginationNextSelector = self.CONFIG["company"]["paginationNextSelector"]
        paginationDisabledSelector = self.CONFIG["company"]["paginationDisabledSelector"]
        searchResultsContainerSelector = self.CONFIG["company"]["searchResultsContainerSelector"]
        paginationContentSelector = self.CONFIG["company"]["paginationContentSelector"]
        jobTitleTypeaHeadSelector = self.CONFIG["company"]["jobTitleTypeaHeadSelector"]

        searchResultHoverableOutletSelector = self.CONFIG[
            "company"]["searchResultHoverableOutletSelector"]

        contentSelector = self.CONFIG["company"]["employeeSelector"]["content"]
        nameSelector = self.CONFIG["company"]["employeeSelector"]["name"]
        designationSelector = self.CONFIG["company"]["employeeSelector"]["designation"]
        companySelector = self.CONFIG["company"]["employeeSelector"]["company"]
        locationSelector = self.CONFIG["company"]["employeeSelector"]["location"]

        allEmployeesEle = self.DRIVER.presenceOfElementLocated(
            allEmployeesSelector)

        companyWebsiteUrl = ""
        companyWebsiteUrlEle = self.DRIVER.findElement(
            companyWebsiteUrlSelector)
        if companyWebsiteUrlEle:
            companyWebsiteUrl = companyWebsiteUrlEle.get_attribute("href")

        # ==========================================================================================
        try:
            allEmployeCount=self.DRIVER.findElement(".ember-view.link-without-visited-and-hover-state").text
        except:
            allEmployeCount=""

        allEmployeCount=allEmployeCount.replace("All employees (", "").\
            replace("See all employees on search results page", "").replace("+", "").replace(")","").rstrip()



        self.DRIVER.click(allEmployeesEle)
        self.DRIVER.sleep(4)

        if "K" not in allEmployeCount and int(allEmployeCount) <=500:

            employeeInformation=[]

            # print("small company auromation")


            try:
                lastPageNo = self.DRIVER.executeScript(self.CONFIG['company'][ 'lastPageNo'])
            except Exception as e:
                # print(e)
                lastPageNo = 1

            # print(f'lastPageNo --> {lastPageNo}')



            for pageNo in range(1, int(lastPageNo) + 1):

                # time.sleep(10)
                self.DRIVER.presenceOfElementLocated(
                    searchResultsContainerSelector)

                self.DRIVER.presenceOfElementLocated(self.CONFIG['company'][ 'paginationSelector'])

                for i in range(2):
                    pageScrollScript = '''let window = document.querySelector('%s');
                                            window.scrollIntoView({
                                                behavior: 'smooth',
                                                block: 'end',
                                                inline: "start"
                                            });''' % paginationSelector
                    self.DRIVER.executeScript(pageScrollScript)

                    self.DRIVER.sleep(3 / (i + 1))

                    searchResultHoverableOutletScript = '''let window = document.querySelector('%s');
                                            window.scrollIntoView({
                                                behavior: 'smooth',
                                                block: 'end',
                                                inline: "start"
                                            });''' % searchResultHoverableOutletSelector
                    self.DRIVER.executeScript(
                        searchResultHoverableOutletScript)

                    self.DRIVER.sleep(3 / (i + 1))

                filteredEmployeeBatchInformationScript = """
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

                filteredEmployeeBatchInformation = self.DRIVER.executeScript(
                    filteredEmployeeBatchInformationScript)

                # print(filteredEmployeeBatchInformation)
                employeeInformation=employeeInformation+filteredEmployeeBatchInformation

                #cliicking Next Page

                try:
                    self.DRIVER.findElement(self.CONFIG['company']['paginationNextSelector']).click()
                except:
                    pass

                # if pageNo==3:break


            df = pd.DataFrame(employeeInformation)
            jobFiltersList = [job for job in jobFilters]
            jobFucctionFilter = df[df['Designation'].str.contains("|".join(jobFiltersList),na=False)]
            jobLevelFilter = jobFucctionFilter[jobFucctionFilter['Designation'].str.contains("|".join(jobLevles),na=False)]
            employeeInformationDF=jobLevelFilter
            employeeInformationDF.drop_duplicates(inplace=True)

            return {
                "company": companyWebsiteUrl,
                "employee": employeeInformationDF
            }


        # ===============================================================================================


        else:



            employeeInformation = []

            jobSelectorClickNeeded = True

            for jobtitle in jobFilters:

                if(jobSelectorClickNeeded):
                    jobSelectorEle = self.DRIVER.presenceOfElementLocated(
                        jobSelector)
                    self.DRIVER.click(jobSelectorEle)
                    self.DRIVER.sleep(1)
                    self.DRIVER.presenceOfElementLocated(jobTitleTypeaHeadSelector)

                jobSelectorClickNeeded = False

                jobTextSelectorEle = self.DRIVER.presenceOfElementLocated(
                    jobTextSelector)
                self.DRIVER.click(jobTextSelectorEle)
                self.DRIVER.sleep(1)

                self.DRIVER.sendKeys(jobTextSelectorEle, jobtitle, 0.5)
                self.DRIVER.enter(jobTextSelectorEle)
                self.DRIVER.sleep(1)

                # ===========================================================
                try:
                    self.DRIVER.presenceOfElementLocated(
                        ".illustration-spots-large.empty-room",3)
                except:
                    pass

                try:
                    allEmploye=self.DRIVER.findElement(".illustration-spots-large.empty-room")
                    if allEmploye != None:
                        allEmploye="absent"
                    else:
                        allEmploye="present"
                except:
                    allEmploye="present"

                # print(f'allEmploye --> {allEmploye}')

                if allEmploye == "absent":
                    # time.sleep(10)
                    jobTitleRemoveEles = self.DRIVER.findElements(
                        jobTitleRemoveSelector)
                    for jobTitleRemoveEle in jobTitleRemoveEles:
                        self.DRIVER.click(jobTitleRemoveEle)
                        self.DRIVER.sleep(1)


                        try:
                            self.DRIVER.presenceOfElementLocated(
                            searchResultsContainerSelector) #error
                        except:
                            pass

                    doEmpScrape = False
                else:
                    doEmpScrape = True


                # ==============================================================================

                try:
                    self.DRIVER.presenceOfElementLocated(
                        searchResultsContainerSelector)
                except:
                    continue

                filteredEmployeeInformation = []
                filteredEmployeeCountToScrape = jobFilters[jobtitle]
                # doEmpScrape = True

                while doEmpScrape:

                    for i in range(2):

                        pageScrollScript = '''let window = document.querySelector('%s');
                            window.scrollIntoView({
                                behavior: 'smooth',
                                block: 'end',
                                inline: "start"
                            });''' % paginationSelector
                        self.DRIVER.executeScript(pageScrollScript)

                        self.DRIVER.sleep(3/(i+1))

                        searchResultHoverableOutletScript = '''let window = document.querySelector('%s');
                            window.scrollIntoView({
                                behavior: 'smooth',
                                block: 'end',
                                inline: "start"
                            });''' % searchResultHoverableOutletSelector
                        self.DRIVER.executeScript(
                            searchResultHoverableOutletScript)

                        self.DRIVER.sleep(3/(i+1))

                    filteredEmployeeBatchInformationScript = """
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
                        }));""" % (contentSelector, nameSelector, designationSelector, companySelector, locationSelector)

                    filteredEmployeeBatchInformation = self.DRIVER.executeScript(
                        filteredEmployeeBatchInformationScript)

                    filteredEmployeeBatchInformation = filteredEmployeeBatchInformation[0:filteredEmployeeCountToScrape]

                    filteredEmployeeInformation = filteredEmployeeInformation + filteredEmployeeBatchInformation

                    isPaginationAvailable = self.DRIVER.findElement(
                        paginationSelector)
                    paginationContent = self.DRIVER.findElements(
                        paginationContentSelector)
                    if isPaginationAvailable and len(paginationContent) > 0:

                        isPaginationNextSelectorDisabledScript = """return document.querySelector('%s').disabled;""" % (
                            paginationNextSelector)
                        isPaginationNextSelectorDisabled = self.DRIVER.executeScript(
                            isPaginationNextSelectorDisabledScript)

                        isPaginationDisabledScript = """return document.querySelectorAll('%s').length > 0;""" % (
                            paginationDisabledSelector)
                        isPaginationDisabled = self.DRIVER.executeScript(
                            isPaginationDisabledScript)

                        if (isPaginationNextSelectorDisabled) or (isPaginationDisabled) or len(filteredEmployeeInformation) >= filteredEmployeeCountToScrape:
                            doEmpScrape = False
                        else:
                            paginationNextSelectorEle = self.DRIVER.presenceOfElementLocated(
                                paginationNextSelector)
                            self.DRIVER.click(paginationNextSelectorEle)
                            self.DRIVER.sleep(1)
                            self.DRIVER.presenceOfElementLocated(
                                searchResultsContainerSelector)
                            jobSelectorClickNeeded = True
                    else:
                        doEmpScrape = False

                employeeInformation = employeeInformation + filteredEmployeeInformation

                jobTitleRemoveEles = self.DRIVER.findElements(
                    jobTitleRemoveSelector)
                for jobTitleRemoveEle in jobTitleRemoveEles:
                    self.DRIVER.click(jobTitleRemoveEle)
                    self.DRIVER.sleep(1)
                    self.DRIVER.presenceOfElementLocated(
                        searchResultsContainerSelector)

            df = pd.DataFrame(employeeInformation)

            jobLevelFilter = df[
                df['Designation'].str.contains("|".join(jobLevles), na=False)]
            employeeInformationDF = jobLevelFilter
            employeeInformationDF.drop_duplicates(inplace=True)

            return {
                "company": companyWebsiteUrl,
                "employee": employeeInformationDF
            }

