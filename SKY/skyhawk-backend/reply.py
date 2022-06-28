import json
import time
from selenium.webdriver.common.by import By
from linkedin_api import Linkedin
import datetime
import csv
from selenium import webdriver
import tldextract
from scraper import *
import re
import os

class  reply():

    def startReply(self):
        replyUrl = self.CONFIG['plugin']['url']
        self.DRIVER.goto(replyUrl, 'secondary')

        self.DRIVER.executeScript(self.CONFIG['plugin']['plus_button'])
        time.sleep(1)
        self.DRIVER.executeScript(self.CONFIG['plugin']['create_contatct'])
        self.DRIVER.presenceOfElementLocated(self.CONFIG['plugin']['savetoReply'])

        os.system("AutoHotkey.ahk")
        time.sleep(5)
        os.system("AutoHotkey.ahk")


    def __init__(self, config, webdriver):
        self.CONFIG = config
        self.DRIVER = webdriver


        # time.sleep(60)

    def remove_emojis(self,data):
        emoj = re.compile("["
                          u"\U0001F600-\U0001F64F"  # emoticons
                          u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                          u"\U0001F680-\U0001F6FF"  # transport & map symbols
                          u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                          u"\U00002500-\U00002BEF"  # chinese char
                          u"\U00002702-\U000027B0"
                          u"\U00002702-\U000027B0"
                          u"\U000024C2-\U0001F251"
                          u"\U0001f926-\U0001f937"
                          u"\U00010000-\U0010ffff"
                          u"\u2640-\u2642"
                          u"\u2600-\u2B55"
                          u"\u200d"
                          u"\u23cf"
                          u"\u23e9"
                          u"\u231a"
                          u"\ufe0f"  # dingbats
                          u"\u3030"
                          "]+", re.UNICODE)

        return re.sub(emoj, '', data)



    def emailFinder(self,fullName,companyWebsite):
        self.DRIVER.switchToTab("secondary")
        # self.startReply()
        self.DRIVER.executeScript("console.clear()")

        fullName =self.remove_emojis(fullName).rstrip()

        firstName,lastName=fullName.split(" ")[0] ,fullName.split(" ")[-1]
        domainName = self.DRIVER.domainName(website=companyWebsite)




        searchButton = "#content-wrap > div.src__Box-sc-1sbtrzs-0.blGwRa > div.src__Box-sc-1sbtrzs-0.sc-fZwumE.kdvBOi > div > div > svg"

        try:
            self.DRIVER.presenceOfElementLocated(searchButton)
        except:
            # print("Error at reply")
            self.startReply()
            self.DRIVER.executeScript("console.clear()")





        emailInputSelector=self.DRIVER.findElement(self.CONFIG['plugin']['input_email'])
        firstNameSelector=self.DRIVER.findElement(self.CONFIG['plugin']['input_fname'])
        lastNameSelector=self.DRIVER.findElement(self.CONFIG['plugin']['input_lname'])

        self.DRIVER.clear(emailInputSelector)
        self.DRIVER.clear(firstNameSelector)
        self.DRIVER.clear(lastNameSelector)


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
            # print(f'email_id_cond --> {timeout}')


            if email_status == "Email not found." or email_id != domainName or time.time() > timeout:
                try:
                    self.DRIVER.executeScript(str(self.CONFIG['plugin']['email_status']).replace("textContent","remove()"))
                except:
                    pass

                break

        if email_id==domainName:
            email_id =""

        # self.DRIVER.get_screenshot_as_file(f"{fullName}.png")

        return email_id





#chekcgit