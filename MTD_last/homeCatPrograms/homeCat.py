from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui
import tldextract
import glob
from pyshadow.main import Shadow
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import numpy as np
import pandas as pd
import csv
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from MTD_last.util import *





def home_category(df):
    url_no = 0

    options = webdriver.ChromeOptions()
    driver_var = webdriver.Chrome(executable_path="chromedriver.exe")
    driver_var.set_window_position(-10000, 0)


    with open("home_cat_output\cat_all_urls.csv","a",newline="",encoding="UTF-8") as fp:
        writer=csv.writer(fp)
        writer.writerow(["Web_id","Home_url","Cat_url1","Cat_url2","Cat_url3","Cat_method"])
# homeurls=df['Company Website'].values
# for clinet_id,homeurl in zip(['1121'],['https://www.currentbody.com/']):
    homecatArray=[]
    for clinet_id,homeurl in zip(df['Web_id'].values,df['Company_Website'].values):
        # print(clinet_id,homeurl)

            # print(homeurl)

            url_no = url_no + 1

            # if url_no == 2:
            #     break

            # homeurl = 'https://www.' + homeurl

            try:
                driver_var.get(homeurl)
                # time.sleep(10)
            except:
                pass

            # homeurl=driver_var.current_url

            page_is_loading(driver_var)

            driver_var.get_screenshot_as_file(f"WebsiteScreenshot/{str(clinet_id)}.png")



            # =========================================================pattenrn 1 cariuma  currentbody
            catlinks = []
            prodlinks = []

            elems = driver_var.find_elements(By.XPATH, "//a[@href]")
            for elem in elems:
                try:
                    link = elem.get_attribute("href")
                except:
                    link = ""

                try:
                    link.replace("#", "")
                except:
                    pass

                if link != None:


                        if '/collections/' in str(link).lower() or '/c/' in str(link).lower() or '/all-collections/' in str(link).lower() or'/collection' in str(link).lower() or 'collection/' in str(link).lower():
                           if  link.startswith(homeurl):
                            catlinks.append(link)

                        elif 'category' in str(link).lower() or 'categories' in str(link).lower() or "showall" in str(link).lower() or "see all" in 'categories' in str(link).lower():
                            if link.startswith(homeurl):
                                catlinks.append(link)
                        elif "shop-all" in str(link).lower() or "best-sellers" in str(link).lower() or "new-arrivals" in str(link).lower() or "see-all" in str(link).lower():
                            if link.startswith(homeurl):
                                catlinks.append(link)

                        elif "shop_all" in str(link).lower() or "best_sellers" in str(link).lower() or "new_arrivals" in str(link).lower() or "see_all" in str(link).lower():
                            if link.startswith(homeurl):
                                catlinks.append(link)

                        elif "view-all" in str(link).lower() or "view_all" in str(link).lower() or "viewall" in str(link).lower() or "view alll" in str(link).lower():
                            if link.startswith(homeurl):
                                catlinks.append(link)

            #keyword xpth logic
            if not catlinks:
                cat_finder_xpath = "//a[contains(text(),'view all') or contains(text(),'View All') or contains(text(),'View all') " \
                                   "or contains(text(),'Best Sellers') or contains(text(),'New Arrivals')  or contains(text(),'New Arrivals') " \
                                   "or contains(text(),'Shop All') or contains(text(),'Shop all')]"

                cat_elems =driver_var.find_elements(By.XPATH,cat_finder_xpath)


                if cat_elems != None :
                    for cat_iteror in cat_elems:

                        try:
                            catlink = cat_iteror.get_attribute("href")
                        except:
                            catlink = ""

                        try:
                            catlink.replace("#", "")
                        except:
                            pass

                        catlink_var =  chck_link(catlink, homeurl)
                        if catlink_var != None and catlink_var !=homeurl  and catlink_var.startswith(homeurl):
                            # print(f"catlink_var {catlink_var}")
                            catlinks.append(catlink_var)

            catlinks = list(np.unique(np.array(catlinks)))
            # print(len(catlinks))
            try:
                cat_url = np.random.choice(catlinks, size=3, replace=False)
                cat_url1, cat_url2, cat_url3 = cat_url[0], cat_url[1], cat_url[2]
                cat_method_ = "keywords matching"



            except:
                cat_url = ""
                cat_url1, cat_url2, cat_url3 = "", "", ""


            if cat_url1 == "" or cat_url2 == "" or cat_url3 == "":
                cat_method_= 'nav a'
                cat_elems = driver_var.find_elements(By.CSS_SELECTOR, "nav a")
                # print(f'cat_elems ==== {cat_elems}')

                if cat_elems != None :
                    for cat_iteror in cat_elems:

                        try:
                            catlink = cat_iteror.get_attribute("href")
                        except:
                            catlink = ""

                        try:
                            catlink.replace("#", "")
                        except:
                            pass

                        catlink_var =  chck_link(catlink, homeurl)
                        if catlink_var != None and catlink_var !=homeurl and catlink_var.startswith(homeurl):
                            # print(f"catlink_var {catlink_var}")

                            catlinks.append(catlink_var)
                            # print(catlinks)

            catlinks = list(np.unique(np.array(catlinks)))
            # print(len(catlinks))
            try:
                cat_url = np.random.choice(catlinks, size=3, replace=False)
                cat_url1, cat_url2, cat_url3 = cat_url[0], cat_url[1], cat_url[2]


            except:
                cat_url = ""
                cat_url1, cat_url2, cat_url3 = "", "", ""



            if cat_url1 == "" or cat_url2 == "" or cat_url3 == "":
                cat_method_ = '[class*="nav"]  a'
                cat_elems = driver_var.find_elements(By.CSS_SELECTOR, '[class*="nav"]  a')

                # print(f'cat_elems ==== {cat_elems}')

                if cat_elems != None :
                    for cat_iteror in cat_elems:

                        try:
                            catlink = cat_iteror.get_attribute("href")
                        except:
                            catlink = ""

                        try:
                            catlink.replace("#", "")
                        except:
                            pass

                        catlink_var =  chck_link(catlink, homeurl)
                        if catlink_var != None and catlink_var !=homeurl and catlink_var.startswith(homeurl):
                            # print(f"catlink_var {catlink_var}")

                            catlinks.append(catlink_var)
                            # print(catlinks)

            catlinks = list(np.unique(np.array(catlinks)))
            # print(len(catlinks))
            try:
                cat_url = np.random.choice(catlinks, size=3, replace=False)
                cat_url1, cat_url2, cat_url3 = cat_url[0], cat_url[1], cat_url[2]




            except:
                cat_url = ""
                cat_url1, cat_url2, cat_url3 = "", "", ""


            if cat_url1 == "" or cat_url2 == "" or cat_url3 == "":
                cat_method_ = 'ul >  li >  a'
                cat_elems = driver_var.find_elements(By.CSS_SELECTOR, '[class*="nav"]  a')

                # print(f'cat_elems ==== {cat_elems}')

                if cat_elems != None:
                    for cat_iteror in cat_elems:

                        try:
                            catlink = cat_iteror.get_attribute("href")
                        except:
                            catlink = ""

                        try:
                            catlink.replace("#", "")
                        except:
                            pass

                        catlink_var = chck_link(catlink, homeurl)
                        if catlink_var != None and catlink_var !=homeurl:
                            # print(f"catlink_var {catlink_var}")

                            catlinks.append(catlink_var)
                            # print(catlinks)

            catlinks = list(np.unique(np.array(catlinks)))
            # print(len(catlinks))
            try:
                cat_url = np.random.choice(catlinks, size=3, replace=False)
                cat_url1, cat_url2, cat_url3 = cat_url[0], cat_url[1], cat_url[2]



            except:
                cat_url = ""
                cat_url1, cat_url2, cat_url3 = "", "", ""


            if cat_url1 == "" or cat_url2 == "" or cat_url3 == "":
                cat_elems = driver_var.find_elements(By.CSS_SELECTOR, '[class*="menu"]  a')
                cat_method_ = '[class*="menu"]  a'

                if cat_elems != None:
                    for cat_iteror in cat_elems:

                        try:
                            catlink = cat_iteror.get_attribute("href")
                        except:
                            catlink = ""

                        try:
                            catlink.replace("#", "")
                        except:
                            pass

                        catlink_var =  chck_link(catlink, homeurl)
                        if catlink_var != None and catlink_var != homeurl and catlink_var.startswith(homeurl) :
                            # print(f"catlink_var {catlink_var}")

                            catlinks.append(catlink_var)
                            # print(catlinks)


            if None not in catlinks :
                catlinks = list(np.unique(np.array(catlinks)))
                # print(len(catlinks))
                try:
                    cat_url = np.random.choice(catlinks, size=3, replace=False)
                    cat_url1, cat_url2, cat_url3 = cat_url[0], cat_url[1], cat_url[2]



                except:
                    cat_url = ""
                    cat_url1, cat_url2, cat_url3 = "", "", ""
                    cat_method_=""


            if cat_url1 != "" and cat_url2 != "" and cat_url3 != "":
                # print(f'({url_no}).  {homeurl} -->cat_url1 : {cat_url1} --> cat_url2 : {cat_url2} --> cat_url3 : {cat_url3}  --> cat_method : {cat_method_}')

                with open("home_cat_output\cat_all_urls.csv", "a", newline="", encoding="UTF-8") as fp:
                    writer = csv.writer(fp)
                    writer.writerow([clinet_id, homeurl, cat_url1, cat_url2, cat_url3,cat_method_])

                homecatArray.append( {
                        "clinet_id" :clinet_id,
                        "homeurl": homeurl,
                        "cat_url1":cat_url1,
                        "cat_url2":cat_url2,
                        "cat_url3":cat_url3})

            else:
                # print(
                    # f'({url_no}).  {homeurl} -->cat_url1 : {None} --> cat_url2 : {None} --> cat_url3 : {None}   --> cat_method : {None}')

                homecatArray.append({
                    "clinet_id": clinet_id,
                    "homeurl": homeurl,
                    "cat_url1": None,
                    "cat_url2": None,
                    "cat_url3": None})

                with open("home_cat_output\cat_all_urls.csv", "a", newline="", encoding="UTF-8") as fp:
                    writer = csv.writer(fp)
                    writer.writerow([clinet_id, homeurl, "None", "None", "None", "None"])

                homecatArray.append({
                                    "clinet_id": clinet_id,
                                    "homeurl": homeurl,
                                     "cat_url1": None,
                                     "cat_url2": None,
                                     "cat_url3": None})

    driver_var.quit()
    return homecatArray
