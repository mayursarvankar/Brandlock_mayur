import json
import time
from selenium.webdriver.common.by import By
from linkedin_api import Linkedin
import datetime
import csv
from selenium import webdriver
import tldextract
from scraper import *

class  reply():
    def __init__(self, config, webdriver):
        self.CONFIG = config
        self.DRIVER = webdriver

    def emailFinder(self,fullName,companyWebsite):

        firstName,lastName=fullName.split(" ")[0] ,fullName.split(" ")[-1]
        domainName = self.DRIVER.domainName(website=companyWebsite)


        replyUrl = self.CONFIG['plugin']['url']
        self.DRIVER.goto(replyUrl, 'secondary')


        self.DRIVER.executeScript(self.CONFIG['plugin']['plus_button'])
        time.sleep(1)
        self.DRIVER.executeScript(self.CONFIG['plugin']['create_contatct'])
        self.DRIVER.presenceOfElementLocated(self.CONFIG['plugin']['savetoReply'])

        emailInputSelector=self.DRIVER.findElement(self.CONFIG['plugin']['input_email'])
        firstNameSelector=self.DRIVER.findElement(self.CONFIG['plugin']['input_fname'])
        lastNameSelector=self.DRIVER.findElement(self.CONFIG['plugin']['input_lname'])


        self.DRIVER.wholesendKey(emailInputSelector, domainName)
        self.DRIVER.wholesendKey(firstNameSelector,firstName)
        self.DRIVER.wholesendKey(lastNameSelector,lastName)

        #clickSercbutton
        self.DRIVER.executeScript(self.CONFIG['plugin']['clinkcing_serach_button'])


        #checkingEmail
        timeout = time.time() + 60  # 1 minutes from now
        while True:

            try:
                email_status = self.DRIVER.executeScript(self.CONFIG['plugin']['email_status'])
            except:
                email_status = ""
            #

            email_id = self.DRIVER.executeScript(self.CONFIG['plugin']['email_finder'])

            # print(f'email_status --> {email_status}')
            # print(f'email_id_cond --> {email_id_cond}')

            if email_status == "Email not found." or email_id != domainName or time.time() > timeout:
                break

        if email_id==domainName:
            email_id =""

        return email_id




    # def reply_driver_config(self):
    #
    #     self.profile_no = self.configData['Hawk_driver']['Chrome_profile_no']
    #     self.chromdriver_exe_path = self.configData['Hawk_driver']['Driver_path']
    #
    #     self.options = webdriver.ChromeOptions()  # Path to your chrome profile
    #     self.options.add_argument(f'--profile-directory=Profile {self.profile_no}')
    #
    #     self.options.add_argument(
    #         "user-data-dir=C:\\Users\\Admin\AppData\\Local\\Google\\Chrome\\User Data")  # Path to your chrome
    #
    #     # options.add_argument('headless')
    #
    #     self.replydriver_obj = webdriver.Chrome(
    #         executable_path=self.chromdriver_exe_path,
    #         options=self.options)
    #
    #     self.replydriver_obj.maximize_window()
    #     # self.replydriver_obj.set_window_position(-10000,0)
    #
    #     return self.replydriver_obj
    #
    # def reply_email_finder(self,driver_obj,fullName,compWebiste):
    #
    #     splitname=fullName.split(" ")
    #     frist_name = splitname[0]
    #     last_name = splitname [-1]
    #     company_domain = tldextract.extract(compWebiste).domain + "." + tldextract.extract(compWebiste).suffix
    #
    #     driver_obj.get(self.configData['reply.io']['plugin'])
    #
    #     time.sleep(2)
    #     # driver_obj.execute_script(f'''{self.configData['reply_selectors']['plus_button']}''')
    #     #
    #     # time.sleep(2)
    #     # # driver_obj.find_element(By.CSS_SELECTOR, "[data-cy=add-menu-create-contact]").click()
    #     # driver_obj.execute_script(f''' {self.configData['reply_selectors']['create_contatct']} ''')
    #     #
    #     # time.sleep(2)
    #     #
    #     # self.email_input = driver_obj.find_element(By.CSS_SELECTOR,
    #     #                                                      self.configData['reply_selectors']['input_email'])
    #     # self.first_name_input = driver_obj.find_element(By.CSS_SELECTOR,
    #     #                                                           self.configData['reply_selectors']['input_fname'])
    #     # self.last_name_input = driver_obj.find_element(By.CSS_SELECTOR,
    #     #                                                          self.configData['reply_selectors']['input_lname'])
    #     #
    #     # self.email_input.send_keys(company_domain)
    #     # self.first_name_input.send_keys(frist_name)
    #     # self.last_name_input.send_keys(last_name)
    #     #
    #     # time.sleep(2)
    #     #
    #     # driver_obj.execute_script(f''' {self.configData['reply_selectors']['clinkcing_serach_button']}''')
    #     # #
    #     # # # chcking email found or not
    #     # timeout = time.time() + 60 * 3  # 3 minutes from now
    #     # while True:
    #     #
    #     #     try:
    #     #         self.email_status = driver_obj.execute_script(
    #     #             f''' {self.configData['reply_selectors']['email_status']} ''')
    #     #     except:
    #     #         self.email_status = ""
    #     #     #
    #     #     # print(f'email_status --> {email_status}')
    #     #
    #     #     self.email_id_cond = driver_obj.execute_script(
    #     #         f''' {self.configData['reply_selectors']['email_finder']} ''')
    #     #
    #     #     # print(f'email_id_cond --> {email_id_cond}')
    #     #
    #     #     if self.email_status == "Email not found." or self.email_id_cond != company_domain or time.time() > timeout:
    #     #         break
    #     #
    #     # #
    #     # # if email_id == company_domain or email_id == "":
    #     # #     try:
    #     # #         driver_obj.execute_script(
    #     # #             ''' document.querySelector("#content-wrap").style.backgroundColor = "#e8e195"  ''')
    #     # #     except:
    #     # #         pass
    #     #
    #     # #
    #     #
    #     # if self.email_id_cond != company_domain:
    #     #     self.email_status_var = "Email Found"
    #     # else:
    #     #     self.email_id_cond=""
    #     #     self.email_status_var = "Email not found"
    #     #
    #     #
    #     #
    #     #
    #     # return self.email_id_cond, self.email_status_var

#
# eid, estatys = reply().reply_email_finder(driver_obj=reply().reply_driver_config(),fullName="Rashmi (Jagasia) Joshi",compWebiste="https://www.blackrock.com")
# # eid, estatys = reply().reply_email_finder(driver_obj=reply().reply_driver_config(),fullName="mayur sarvankar",compWebiste="")
# print(eid,estatys)
#
