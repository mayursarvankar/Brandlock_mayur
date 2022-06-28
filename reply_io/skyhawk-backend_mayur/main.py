from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import glob
from selenium.webdriver.common.action_chains import ActionChains
import os
from selenium.common.exceptions import TimeoutException
import json
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from linkedin import *
from scraper import *
from reply import *

# Start : Load Config #
DIR = os.getcwd()
CONFIG = json.load(open(DIR+'/config.json'))
CHROME = CONFIG['chrome']
DB = CONFIG['db']
LINKEDIN_SALES = CONFIG['sales']
REPLY_IO = CONFIG['reply.io']
# End : Load Config #


# while True:


# Start : Initialise driver #
scraperDriver = scraper(CHROME)
if scraperDriver.getDriver() == None:
    pass
else:
    linkedinObject = linkedin(LINKEDIN_SALES, scraperDriver)
    isLoggedIn = linkedinObject.login()
    if isLoggedIn:
        company = "https://www.linkedin.com/sales/company/24979909"  #BL
        # company = "https://www.linkedin.com/sales/company/1441"
        employeeBatchInformation =linkedinObject.visitCompany(company)


        for emp in employeeBatchInformation:

            replyObject = reply(REPLY_IO, scraperDriver)
            emailID = replyObject.emailFinder(fullName=emp['Name'],companyWebsite="https://www.brandlock.io/")

            print(f"======================================================")
            print(f"Name         : {emp['Name']}\n"
                  f"emailID      : {emailID}\n"
                  f"Company      : {emp['Company']}\n"
                  f"Designation  : {emp['Designation']}\n"
                  f"Location     : {emp['Location']}")


        pass
    else:
        print("Linkedin Login Error")
        scraperDriver.quit()
    try:
        pass
    except Exception as e:
        print(e)
        scraperDriver.quit()




# #start : Initialise driver #
# scraperDriver = scraper(CHROME)
# if scraperDriver.getDriver() == None:
#     pass
# else:
#     replyObject = reply(REPLY_IO, scraperDriver)
#     emailID = replyObject.emailFinder(fullName="Rashmi (Jagasia) Joshi",companyWebsite="https://www.blackrock.com/")
#     print(f'emailID {emailID}')