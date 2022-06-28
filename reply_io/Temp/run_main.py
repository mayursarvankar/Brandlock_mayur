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
from run_reply import *
from main import *



class hawak():
    def __init__(self):
        self.configData = json.load(open('linkedi_inputs/config.json'))
        # remove this
        # self.companyInfo = self.configData['company_info']
        self.companyInfo = ['https://www.linkedin.com/sales/company/4764']
        # self.companyInfo = ['https://www.linkedin.com/sales/company/24979909',
        #                     'https://www.linkedin.com/sales/company/4764']

        # self.companyInfo=[
        #                     "https://www.linkedin.com/sales/company/110290",
        #                     "https://www.linkedin.com/sales/company/12906074",
        #                     "https://www.linkedin.com/sales/company/2795",
        #                     "https://www.linkedin.com/sales/company/18780"]


    def loginInfo(self):
        self.username = self.configData['sales']['login']['username']
        self.password = self.configData['sales']['login']['password']

        return self.username,self.password

    def jobTitleInfo(self):
        # self.jobTitlesList = self.configData['sales']['company']['jobFilters']
        self.jobTitlesList= {"sales":  25  ,
                              "Brand":  25 ,
                             "CEO":25,
                             "President":25}

        return self.jobTitlesList

    def csvConfig(self):
        with open("linkedi_ouptut\\linke_op.csv", "a", newline="", encoding="UTF-8") as fp:
            writer = csv.writer(fp)
            writer.writerow(
                ["Full_name", "Email_id", "Job_title", "Company_name", "Company_website",
                 "Location", "Email_status", "Linkedin_url", "Datetime"])


    def databaseConfig(self):
        pass



    #
    def sendingKeyInput(self,inputSelector,key,delay):
        for word in key:
            inputSelector.send_keys(word)
            time.sleep(delay)



    def waitIfElementPresent(self,driver,element):
        while True:
            try:
                elementStatus=driver.find_element(By.CSS_SELECTOR,element)
            except:
                elementStatus = None

            if elementStatus!=None:
                break

    def scrollingDownPage(self,driver):
        last_height = driver.execute_script(f''' {self.configData['sales']['company']['pageHeight']} ''')

        time.sleep(5)


        while True:
            # Scroll down to bottom

            lastEmpID = driver.execute_script(f'''{self.configData['sales']['company']['lastEmpID']}  ''')

            # driver_full_name=driver.find_element(By.CSS_SELECTOR,)

            scrollOption = "{behavior:'smooth'}"
            lastEmpScroll = driver.execute_script(
                f''' document.getElementById("{lastEmpID}").scrollIntoView({scrollOption}); ''')

            # Wait to load page
            time.sleep(2)
            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script(f''' {self.configData['sales']['company']['pageHeight']} ''')

            # print(f"new_height : {new_height} --> last heigt {last_height} ")
            if new_height == last_height:
                break
            last_height = new_height



    def insertingJobTitle(self,driver,jobTitlesList):
        driver.find_element(By.XPATH,
                                         self.configData['sales']['company']['addJobTitleButton']).click()

        self.inputBoxJobTitle = driver.find_element(By.CSS_SELECTOR,
                                                                 self.configData['sales']['company'][
                                                                     'inputJobTitle'])

        for jobtitle in jobTitlesList:
            self.sendingKeyInput(inputSelector=self.inputBoxJobTitle, key=jobtitle, delay=0.01)
            self.inputBoxJobTitle.send_keys(Keys.ENTER)




    def hawkDriverConfig(self):
        self.profile_no = self.configData['Hawk_driver']['Chrome_profile_no']
        self.chromdriver_exe_path = self.configData['Hawk_driver']['Driver_path']

        # self.options = webdriver.ChromeOptions()  # Path to your chrome profile
        # self.options.add_argument(f'--profile-directory=Profile {self.profile_no}')
        #
        # self.options.add_argument(
        #     "user-data-dir=C:\\Users\\Admin\AppData\\Local\\Google\\Chrome\\User Data")  # Path to your chrome
        #
        # # options.add_argument('headless')
        #
        # self.hawkDriver_obj = webdriver.Chrome(
        #     executable_path=self.chromdriver_exe_path,
        #     options=self.options)

        options = FirefoxOptions()
        self.hawkDriver_obj = webdriver.Firefox(options=options)

        self.linkedinTab = self.hawkDriver_obj.current_window_handle
        self.hawkDriver_obj.execute_script(f"window.open('about:blank','tab1');")
        self.replyTab = self.hawkDriver_obj.window_handles[1]

        self.hawkDriver_obj.maximize_window()

        # self.hawkDriver_obj.set_window_position(-10000,0)

        return self.hawkDriver_obj

    def runHawk(self):
       self.loginInfo()
       self.jobTitleInfo()
       self.csvConfig()
       self.hawkDriverConfig()
       #
       #
       #loginintolinked
       self.hawkDriver_obj.switch_to.window(self.linkedinTab)

       self.hawkDriver_obj.get(self.configData['sales']['login']['url'])

       self.usernameSelector =self.configData['sales']['login']['usernameSelector']
       self.passwordSelector=self.configData['sales']['login']['passwordSelector']

       self.logIfrmae=self.hawkDriver_obj.find_element(By.CSS_SELECTOR,self.configData['sales']['login']['logInIfrmaeSelector'])
       self.hawkDriver_obj.switch_to.frame(self.logIfrmae)

       self.inputUsernmae=self.hawkDriver_obj.find_element(By.CSS_SELECTOR, self.usernameSelector)
       self.inputPasswprd=self.hawkDriver_obj.find_element(By.CSS_SELECTOR,self.passwordSelector)


       self.inputUsernmae.clear()
       self.inputPasswprd.clear()

       self.sendingKeyInput(inputSelector = self.inputUsernmae,key = self.configData['sales']['login']['username'],delay=0.1)
       self.sendingKeyInput(inputSelector = self.inputPasswprd,key  =self.configData['sales']['login']['password'],delay=0.1)
       self.inputUsernmae.submit()

       # self.waitIfElementPresent(driver=self.hawkDriver_obj,element=self.configData['sales'] ['company']['navSearchBoxSelector'])

       time.sleep(5)

        #getingCompanyStaff
       for linkedinCompanyUrl in self.companyInfo:
           self.hawkDriver_obj.switch_to.window(self.linkedinTab)

           self.hawkDriver_obj.get(linkedinCompanyUrl)


           self.waitIfElementPresent(driver=self.hawkDriver_obj,element=".ember-view.link-without-visited-and-hover-state")

           # time.sleep(5)

           #getingCompany_info
           try:
               self.companyName=self.hawkDriver_obj.find_element(By.CSS_SELECTOR,self.configData['sales']['company']['companyNameSelector']).text
           except:
               self.companyName =""

           try:
               self.companyWebsite=self.hawkDriver_obj.find_element(By.CSS_SELECTOR,self.configData['sales']['company']['companyWebsiteSelector']).get_attribute("href")
           except:
               self.companyWebsite =""

           print(f"======================================={self.companyName}============================================")


           #allEmployeeButton
           self.hawkDriver_obj.find_element(By.CSS_SELECTOR,self.configData['sales']['company']['allEmployeesSelector']).click()
           self.waitIfElementPresent(driver=self.hawkDriver_obj,element='.flex.justify-center.align-items-center')

           #clickonallfilters
           self.hawkDriver_obj.find_element(By.CSS_SELECTOR,".artdeco-button.artdeco-button--muted.artdeco-button--2.artdeco-button--tertiary.mb4").click()

           #clciksenioritylevl
           time.sleep(2)
           self.hawkDriver_obj.find_element(By.CSS_SELECTOR ,"fieldset:nth-child(2) > div > fieldset:nth-child(3) > div > button").click()
           time.sleep(1)

           self.hawkDriver_obj.execute_script(''' document.querySelector('[title *="Include “VP"] ').click() ''')
           self.hawkDriver_obj.execute_script(''' document.querySelector('[title *="Include “CXO"] ').click() ''')
           self.hawkDriver_obj.execute_script(''' document.querySelector('[title *="Include “Director"] ').click() ''')
           self.hawkDriver_obj.execute_script(''' document.querySelector('[title *="Include “Manager"] ').click() ''')


           time.sleep(5)



           # ##inserting jobtitle
           # self.hawkDriver_obj.find_element(By.CSS_SELECTOR,self.configData['sales']['company']['addJobTitleButton']).click()
           self.hawkDriver_obj.find_element(By.CSS_SELECTOR,"fieldset:nth-child(2) > div > fieldset:nth-child(2) > div > button").click()
           #
           self.inputBoxJobTitle = self.hawkDriver_obj.find_element(By.CSS_SELECTOR,
                                                                    self.configData['sales']['company'][
                                                                        'inputJobTitle'])



           for jobtitle,joblimit in self.jobTitlesList.items():

               #removing seniority level
               if jobtitle == "CEO":
                   self.hawkDriver_obj.execute_script('''document.querySelector('[title *= "Remove Seniority level filter: “VP"]').click()''')
                   self.hawkDriver_obj.execute_script('''document.querySelector('[title *= "Remove Seniority level filter: “Director"]').click()''')
                   self.hawkDriver_obj.execute_script('''document.querySelector('[title *= "Remove Seniority level filter: “CXO"]').click()''')
                   self.hawkDriver_obj.execute_script('''document.querySelector('[title *= "Remove Seniority level filter: “Manager"]').click()''')

                   self.hawkDriver_obj.find_element(By.CSS_SELECTOR,
                                                    "fieldset:nth-child(2) > div > fieldset:nth-child(2) > div > button").click()
                   #
                   self.inputBoxJobTitle = self.hawkDriver_obj.find_element(By.CSS_SELECTOR,
                                                                            self.configData['sales']['company'][
                                                                                'inputJobTitle'])
                   time.sleep(5)

               #insertingJobtilte
               self.sendingKeyInput(inputSelector=self.inputBoxJobTitle,key=jobtitle,delay=0.1)
               self.inputBoxJobTitle.send_keys(Keys.ENTER)
               self.scrollingDownPage(self.hawkDriver_obj)

               #scrapping
               #     #getinngEmplyeinfo
               try:
                   self.employeeContent=self.hawkDriver_obj.find_elements(By.CSS_SELECTOR,self.configData['sales']['company'][
                       'employeeSelector']['content'])
               except:
                   self.employeeContent = []


               empNo =0
               for empInfo in self.employeeContent:
                   empNo += 1
                   print(f"---------------------------------------------{empNo}---------------------------------------------")

                   try:
                       self.empFullName=empInfo.find_element(By.CSS_SELECTOR,self.configData['sales']['company'][
                           'employeeSelector']['name']).text
                   except:
                       self.empFullName = ""

                   try:
                       self.empDesignaton = empInfo.find_element(By.CSS_SELECTOR, self.configData['sales']['company'][
                           'employeeSelector']['designation']).text
                   except:
                       self.empDesignaton=""


                   #replyEmaildinding
                   #
                   # self.hawkDriver_obj.switch_to.window(self.replyTab)
                   # self.empEmailID,self.empEmailStatus=reply().reply_email_finder(driver_obj=self.hawkDriver_obj,
                   #                                                                fullName=self.empFullName,
                   #                                                                compWebiste=self.companyWebsite)
                   # time.sleep(1)
                   # self.hawkDriver_obj.switch_to.window(self.linkedinTab)

                   #-------------------------------------------------------



                   try:
                       self.empLocation=empInfo.find_element(By.CSS_SELECTOR,self.configData['sales']['company'][
                           'employeeSelector']['location']).text
                   except:
                       self.empLocation=""


                   try:
                       self.empCompanyName = empInfo.find_element(By.CSS_SELECTOR,self.configData['sales']['company'][
                           'employeeSelector']['company']).text
                   except:
                       self.empCompanyName = ""


                   try:
                       self.empLinkedinUrl=empInfo.find_element(By.CSS_SELECTOR,self.configData['sales']['company'][
                           'employeeSelector']['name']).get_attribute("href")
                   except:
                       self.empLinkedinUrl = ""


                   try:
                       self.dateTime = str(datetime.datetime.now()).split('.')[0]
                   except:
                       self.dateTime = ""


                   print(f"Full Name        : {self.empFullName}\n"
                         f"Job Designation  : {self.empDesignaton}\n"
                         # f"Email Id         : {self.empEmailID}\n"
                         # f"Email Status     : {self.empEmailStatus}\n"
                         f"Location         : {self.empLocation}\n"
                         f"Comapny Name     : {self.empCompanyName}\n"
                         f"Linkedin Url     : {self.empLinkedinUrl}\n"
                         f"dateTime         : {self.dateTime}")


                   if empNo == joblimit:break
           #


               #removingJobTitlte
               romovingSelector =self.configData['sales']['company']['removeJobTtitle']
               self.hawkDriver_obj.execute_script(f'''document.querySelector("{romovingSelector}").click() ''')


               time.sleep(10)









H=hawak().runHawk()



