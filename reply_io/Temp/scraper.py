from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui
import tldextract
import  glob
from pyshadow.main import Shadow
from selenium.webdriver.common.action_chains import ActionChains
import os
from selenium.common.exceptions import TimeoutException
import json
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import csv
# from run_reply import *
from main import *
from Util import  *


class Scraper():
    def __init__(self):
        pass

    def hawkDriverConfig(self):
        self.profile_no = self.configData['Hawk_driver']['Chrome_profile_no']
        self.chromdriver_exe_path = self.configData['Hawk_driver']['Driver_path']

        self.options = webdriver.ChromeOptions()  # Path to your chrome profile
        self.options.add_argument(f'--profile-directory=Profile {self.profile_no}')

        self.options.add_argument(
            "user-data-dir=C:\\Users\\Admin\AppData\\Local\\Google\\Chrome\\User Data")  # Path to your chrome

        # options.add_argument('headless')

        self.hawkDriver_obj = webdriver.Chrome(
            executable_path=self.chromdriver_exe_path,
            options=self.options)

        # options = FirefoxOptions()
        # self.hawkDriver_obj = webdriver.Firefox(options=options)

        self.linkedinTab = self.hawkDriver_obj.current_window_handle
        self.hawkDriver_obj.execute_script(f"window.open('about:blank','tab1');")
        self.replyTab = self.hawkDriver_obj.window_handles[1]

        self.hawkDriver_obj.maximize_window()

        # self.hawkDriver_obj.set_window_position(-10000,0)

        return self.hawkDriver_obj



    def scrollingDownPage(self,driver):
        last_height = driver.execute_script(f''' {self.configData['sales']['company']['pageHeight']} ''')

        while True:
            # Scroll down to bottom

            lastEmpID = driver.execute_script(f'''{self.configData['sales']['company']['lastEmpID']}  ''')

            # driver_full_name=driver.find_element(By.CSS_SELECTOR,)

            scrollOption = "{behavior:'smooth'}"
            lastEmpScroll = driver.execute_script(
                f''' document.getElementById("{lastEmpID}").scrollIntoView({scrollOption}); ''')

            # Wait to load page
            time.sleep(1)
            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script(f''' {self.configData['sales']['company']['pageHeight']} ''')

            # print(f"new_height : {new_height} --> last heigt {last_height} ")
            if new_height == last_height:
                break
            last_height = new_height



    def runScraper(self,driver):

        #variable Declaraion

        self.configData =CONFIG

        self.companyInfo = ['https://www.linkedin.com/sales/company/24979909',
                            'https://www.linkedin.com/sales/company/4764']

        self.jobTitlesList = ['Head Product']

        self.hawkDriver_obj = driver


        for linkedinCompanyUrl in self.companyInfo:

            self.hawkDriver_obj.get(linkedinCompanyUrl)

            Util().waitIfElementPresent(driver=self.hawkDriver_obj,
                                      element=".ember-view.link-without-visited-and-hover-state")

            # time.sleep(5)

            # getingCompany_info
            try:
                self.companyName = self.hawkDriver_obj.find_element(By.CSS_SELECTOR,
                                                                    self.configData['sales']['company'][
                                                                        'companyNameSelector']).text
            except:
                self.companyName = ""

            try:
                self.companyWebsite = self.hawkDriver_obj.find_element(By.CSS_SELECTOR,
                                                                       self.configData['sales']['company'][
                                                                           'companyWebsiteSelector']).get_attribute(
                    "href")
            except:
                self.companyWebsite = ""

            print(
                f"======================================={self.companyName}============================================")

            # allEmployeeButton
            self.hawkDriver_obj.find_element(By.CSS_SELECTOR,
                                             self.configData['sales']['company']['allEmployeesSelector']).click()
            Util().waitIfElementPresent(driver=self.hawkDriver_obj, element='.flex.justify-center.align-items-center')

            # ##inserting jobtitle
            self.hawkDriver_obj.find_element(By.CSS_SELECTOR,
                                             self.configData['sales']['company']['addJobTitleButton']).click()

            self.inputBoxJobTitle = self.hawkDriver_obj.find_element(By.CSS_SELECTOR,
                                                                     self.configData['sales']['company'][
                                                                         'inputJobTitle'])

            for jobtitle in self.jobTitlesList:
                Util().sendingKeyInput(inputSelector=self.inputBoxJobTitle, key=jobtitle, delay=0.2)
                self.inputBoxJobTitle.send_keys(Keys.ENTER)

            # pagination

            Util().waitIfElementPresent(driver=self.hawkDriver_obj, element=self.configData['sales']['company'][
                'paginationSelector'])

            # time.sleep(10)
            try:
                self.lastPageNo = self.hawkDriver_obj.execute_script(self.configData['sales']['company'][
                                                                         'lastPageNo'])
            except Exception as e:
                # print(e)
                self.lastPageNo = 1

            self.lastPageNo = int(self.lastPageNo)

            empNo = 0
            for pageNo in range(1, self.lastPageNo + 1):

                # scrollingdownpage
                time.sleep(5)
                # self.hawkDriver_obj.execute_script(''' document.querySelector('.artdeco-pagination').scrollIntoView({behavior:'smooth'}); ''')
                self.scrollingDownPage(driver=self.hawkDriver_obj)

                print(f'pageNo -- > {pageNo}')

                Util().waitIfElementPresent(driver=self.hawkDriver_obj, element=self.configData['sales']['company'][
                    'paginationSelector'])

                time.sleep(5)

                # getinngEmplyeinfo
                try:
                    self.employeeContent = self.hawkDriver_obj.find_elements(By.CSS_SELECTOR,
                                                                             self.configData['sales']['company'][
                                                                                 'employeeSelector']['content'])
                except:
                    self.employeeContent = []

                for empInfo in self.employeeContent:
                    empNo += 1
                    print(
                        f"---------------------------------------------{empNo}---------------------------------------------")

                    try:
                        self.empFullName = empInfo.find_element(By.CSS_SELECTOR, self.configData['sales']['company'][
                            'employeeSelector']['name']).text
                    except:
                        self.empFullName = ""

                    try:
                        self.empDesignaton = empInfo.find_element(By.CSS_SELECTOR, self.configData['sales']['company'][
                            'employeeSelector']['designation']).text
                    except:
                        self.empDesignaton = ""

                    # replyEmaildinding

                    self.hawkDriver_obj.switch_to.window(self.replyTab)
                    self.empEmailID, self.empEmailStatus = reply().reply_email_finder(driver_obj=self.hawkDriver_obj,
                                                                                      fullName=self.empFullName,
                                                                                      compWebiste=self.companyWebsite)
                    time.sleep(1)
                    self.hawkDriver_obj.switch_to.window(self.linkedinTab)

                    # -------------------------------------------------------

                    try:
                        self.empLocation = empInfo.find_element(By.CSS_SELECTOR, self.configData['sales']['company'][
                            'employeeSelector']['location']).text
                    except:
                        self.empLocation = ""

                    try:
                        self.empCompanyName = empInfo.find_element(By.CSS_SELECTOR, self.configData['sales']['company'][
                            'employeeSelector']['company']).text
                    except:
                        self.empCompanyName = ""

                    try:
                        self.empLinkedinUrl = empInfo.find_element(By.CSS_SELECTOR, self.configData['sales']['company'][
                            'employeeSelector']['name']).get_attribute("href")
                    except:
                        self.empLinkedinUrl = ""

                    try:
                        self.dateTime = str(datetime.datetime.now()).split('.')[0]
                    except:
                        self.dateTime = ""

                    print(f"Full Name        : {self.empFullName}\n"
                          f"Job Designation  : {self.empDesignaton}\n"
                          f"Email Id         : {self.empEmailID}\n"
                          f"Email Status     : {self.empEmailStatus}\n"
                          f"Location         : {self.empLocation}\n"
                          f"Comapny Name     : {self.empCompanyName}\n"
                          f"Linkedin Url     : {self.empLinkedinUrl}\n"
                          f"dateTime         : {self.dateTime}")

                    with open("linkedi_ouptut\\linke_op.csv", "a", newline="", encoding="UTF-8") as fp:
                        writer = csv.writer(fp)
                        writer.writerow(
                            [self.empFullName, self.empEmailID, self.empDesignaton, self.companyName,
                             self.companyWebsite,
                             self.empLocation, self.empEmailStatus, self.empLinkedinUrl, self.dateTime])

                    if empNo == 2: break

                    return self.empFullName, self.empEmailID, self.empDesignaton, self.companyName,self.companyWebsite,self.empLocation, self.empEmailStatus, self.empLinkedinUrl, self.dateTime



                # chengingnextpage

                try:
                    self.hawkDriver_obj.find_element(By.CSS_SELECTOR, self.configData['sales']['company'][
                        'paginationNextSelector']).click()
                except:
                    pass

                if pageNo == 1: break