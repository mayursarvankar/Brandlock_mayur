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

from reply import  *
from DB import *
import csv
import datetime

# Start : Load Config #
DIR = os.getcwd()
CONFIG = json.load(open(DIR+'/config.json'))
CHROME = CONFIG['chrome']
DB = CONFIG['db']
LINKEDIN_SALES = CONFIG['sales']
REPLY_IO = CONFIG['reply.io']

# End : Load Config #




# # Start : Initialise driver #
scraperDriver = scraper(CHROME)
if scraperDriver.getDriver() == None:
    pass
else:
    linkedinObject = linkedin(LINKEDIN_SALES, scraperDriver)
    replyObject = reply(REPLY_IO, scraperDriver)
    isLoggedIn = linkedinObject.login()

    if isLoggedIn:


    # ==============================================================================

        with open("Hawk_Op.csv", "a", newline="", encoding="UTF-8") as fp:
            writer = csv.writer(fp)
            writer.writerow(["Name", 	"Designation","Location",	"emailID",	"Company",	"Website",	"campId"])


        Data = {12349:[

            # "https://www.linkedin.com/sales/company/24979909",  # small comp
                    # "https://www.linkedin.com/sales/company/18641"  #big compamies
                    # # "https://www.linkedin.com/sales/company/13392707" #very small comp
                    "https://www.linkedin.com/sales/company/12178112",
                    "https://www.linkedin.com/sales/company/8567",
                    "https://www.linkedin.com/sales/company/113288",
                    "https://www.linkedin.com/sales/company/18109183",
                    "https://www.linkedin.com/sales/company/5225618",
                    "https://www.linkedin.com/sales/company/10466819",
                    "https://www.linkedin.com/sales/company/41722437",
                    "https://www.linkedin.com/sales/company/7001946",
                    "https://www.linkedin.com/sales/company/1175330",
                    "https://www.linkedin.com/sales/company/162683",
                    "https://www.linkedin.com/sales/company/992923",
                    "https://www.linkedin.com/sales/company/54663",
                    "https://www.linkedin.com/sales/company/8989",
                    "https://www.linkedin.com/sales/company/1461374",
                    "https://www.linkedin.com/sales/company/2304980",
                    "https://www.linkedin.com/sales/company/1056303",
                    "https://www.linkedin.com/sales/company/2338722",
                    "https://www.linkedin.com/sales/company/5542316",
                    "https://www.linkedin.com/sales/company/98418",
                    "https://www.linkedin.com/sales/company/19010",
                    "https://www.linkedin.com/sales/company/18222555",
                    "https://www.linkedin.com/sales/company/2490019",
                    "https://www.linkedin.com/sales/company/1237060",
                    "https://www.linkedin.com/sales/company/7685155",
                    "https://www.linkedin.com/sales/company/74359099"

        ]
                }
        #while dbchecker if linkedStatus == "" update "Complete" after scrapping




        for campId, companyList in Data.items():
            for company in companyList:
                print("===============================================================")
                companyInformation = linkedinObject.visitCompany(company)

                empInfo= companyInformation['employee']
                compWebsite=companyInformation['company']



                print(f"count of employe {len(empInfo)}")


                # replyObject.startReply()
                #replyIo start
                rowNo=0
                for index,emp in empInfo.iterrows():
                            rowNo=rowNo + 1

                            print(f"----------------------------{rowNo}--------------------------------------")


                            emailID = replyObject.emailFinder(fullName=emp['Name'], companyWebsite=companyInformation['company'])
                            # emailID ="emailID"

                            Datetime_var = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

                            print(f"Name        --> {emp['Name']}\n"
                                  f"Designation --> {emp['Designation']}\n"
                                  f"Location    --> {emp['Location']}\n"
                                  f"Company     --> {emp['Company']}\n"
                                  f"Website     --> {compWebsite}\n"
                                  f"Email Id    --> {emailID}\n"
                                  f"Date Time   --> {Datetime_var}")

                            with open("Hawk_Op.csv", "a", newline="", encoding="UTF-8") as fp:
                                writer = csv.writer(fp)
                                writer.writerow([emp['Name'], emp['Designation'], emp['Location'], emailID, emp['Company'], compWebsite, campId])

                            #insertingINTODB
                            # storingTup = (emp['Name'], emp['Designation'], emp['Location'],emailID, emp['Company'], compWebsite, campId)
                            #
                            #
                            # Database().insertTableRows(tableName="Hawk", insertValuTup=storingTup)



    else:
        print("Linkedin Login Error")
        scraperDriver.quit()
    try:
        pass
    except Exception as e:
        print(e)
        scraperDriver.quit()


scraperDriver.quit()