


from msedge.selenium_tools import Edge, EdgeOptions
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui
import tldextract
import  glob
from pyshadow.main import Shadow
from selenium.webdriver.common.action_chains import ActionChains
import pandas
import os
import csv

with open("linke_op.csv", "a", newline="", encoding="UTF-8") as fp:
    writer = csv.writer(fp)
    writer.writerow(
        ["Full_name", "Job_title", "Company_name", "Company_website", "Linkedin_url"])

def presenceOfElementLocated(selector,driver):
    ele = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    return ele


def scrollingDownPage(driver):
    last_height = driver.execute_script(f''' return document.querySelector(".org-grid__content-height-enforcer").scrollHeight ''')

    time.sleep(5)
    # print(last_height)

    while True:
        # Scroll down to bottom

        # lastEmpID = driver.execute_script(f'''{self.configData['sales']['company']['lastEmpID']}  ''')
        lastEmpID = ".scaffold-finite-scroll__content > ul >li:last-child"


        # driver_full_name=driver.find_element(By.CSS_SELECTOR,)

        for i in range(0,2):
            scrollOption = "{behavior:'smooth'}"
            lastEmpScroll = driver.execute_script(
                f''' document.querySelector("{lastEmpID}").scrollIntoView({scrollOption}); ''')

        # Wait to load page
        time.sleep(3)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script(f''' return document.querySelector(".org-grid__content-height-enforcer").scrollHeight ''')

        # print(f"new_height : {new_height} --> last heigt {last_height} ")
        if new_height == last_height:
            break
        last_height = new_height


jobTypeCategory=[
            "CEO",
            "President",
            "CMO",
            "CTO",
            "CIO",
            "COO",
            "Chief",
            "Founder",
            "DTC",
            "Omnichannel",
            "UI/UX",
            "User experience",
            "Marketing",
            "Ecommerce",
            "E-commerce",
            "Online",
            "Digital",
            "Brand",
            "Design",
            "Product",
            "Finance",
            "Customer",
            "Growth",
            "Performance",
            "Sales",
            "Analytics",
            "Third party",
            "Marketplace"
        ]

jobLevel = [
    "CEO",
    "President",
    "CMO",
    "CTO",
    "CIO",
    "COO",
    "Chief",
    "Founder",
    "Head",
    "Director",
    "VP",
    "Vice President",
    "SVP",
    "EVP",
    "AVP",
    "Manager"]


# options = webdriver.ChromeOptions()  # Path to your chrome profile
# # options.add_argument('--headless')
#
# options.add_argument('--profile-directory=Profile 11')
# options.add_argument("user-data-dir=C:\\Users\\Admin\AppData\\Local\\Google\\Chrome\\User Data")  # Path to your chrome profile
#
# driver_obj = webdriver.Chrome(executable_path=r"C:/Users/Admin/PycharmProjects/db_conection_screenshot/chromedriver.exe", options=options)
# driver_obj.maximize_window()



edge_options = EdgeOptions()
edge_options.use_chromium = True

edge_options.add_argument('user-data-dir=C:\\Users\\admin\\AppData\\Local\\Microsoft\\Edge\\User Data')

#Here you specify the actual profile folder
edge_options.add_argument("profile-directory=Profile 2")

edge_options.binary_location = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
driver_obj = Edge(options = edge_options, executable_path = "msedgedriver.exe")

Data={"altar'd-state" : "https://www.linkedin.com/company/altar'd-state/"
      }

for compName,linkCompUrl in Data.items():

    opData=[]

    print("==========================================================================================================")
    driver_obj.get(linkCompUrl)

    presenceOfElementLocated(".msg-overlay-bubble-header__details.flex-row.align-items-center.ml1",driver_obj)
    # time.sleep(5)
    driver_obj.find_element(By.CSS_SELECTOR,'.org-page-navigation__items > li > a[href *="people"]').click()

    compWebsite=driver_obj.find_element(By.CSS_SELECTOR,".ember-view.org-top-card-primary-actions__action").get_attribute("href")
    scrollingDownPage(driver_obj)
    content= driver_obj.find_elements(By.CSS_SELECTOR,".org-people-profile-card__profile-info")

    empNo=0
    for emp in content:

        try:
            empName=emp.find_element(By.CSS_SELECTOR,".artdeco-entity-lockup__title.ember-view > a").text
        except:
            empName="LinkedIn Member"

        try:
            profilUrl=emp.find_element(By.CSS_SELECTOR,".artdeco-entity-lockup__title.ember-view > a").get_attribute("href")
        except:
            profilUrl=""


        try:
            empJobtitle=emp.find_element(By.CSS_SELECTOR,".org-people-profile-card__profile-info  .artdeco-entity-lockup__subtitle.ember-view").text
            # empJobtitle=empJobtitle.replace(empJobtitle[empJobtitle.find(" at "):], "").rstrip()
        except:
            empJobtitle=""



        dataDict={"empName":empName,"profilUrl":profilUrl,"empJobtitle":empJobtitle,
                  "compWebsite":compWebsite,"compName":compName}
        opData.append(dataDict)

    manindf=pd.DataFrame(opData)
    df3=manindf[manindf['empJobtitle'].str.contains("|".join(jobTypeCategory)) ]
    df2=df3[df3['empJobtitle'].str.contains("|".join(jobLevel)) ]
    # df3=pd.concat(df1,df2)
    # df=df[df['empJobt,itle'].str.contains(r'(?=.*Marketing)(?=.*Brand)',regex=True)]

    for empName,profilUrl,empJobtitle,compWebsite,compName in zip(df2['empName'].values,df2['profilUrl'].values,df2['empJobtitle'].values,
                df2['compWebsite'].values,df2['compName'].values):

        empNo = empNo + 1
        print(
            f"---------------------------------------{empNo}-------------------------------------------")
        print(f"empName     --> {empName}")
        print(f"profilUrl   --> {profilUrl}")
        print(f"empJobtitle --> {empJobtitle}")
        print(f"compWebsite --> {compWebsite}")
        print(f"compName    --> {compName}")

    # for l in df1['empJobtitle'].values:
    #     print(l)

    # for emp in opData:
    #     print(emp)
        # print(
        #     f"---------------------------------------{empNo}-------------------------------------------")
        # print(f"empName     --> {empName}")
        # print(f"profilUrl   --> {profilUrl}")
        # print(f"empJobtitle --> {empJobtitle}")
        # print(f"compWebsite --> {compWebsite}")
        # print(f"compName    --> {compName}")
        #
        # with open("linke_op.csv", "a", newline="", encoding="UTF-8") as fp:
        #     writer = csv.writer(fp)
        #     writer.writerow(
        #         [empName, empJobtitle, compName, compWebsite, profilUrl])
        # # break
        # # empNo = empNo + 1
        # break









