
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
from bs4 import BeautifulSoup
import numpy as np
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pandas as pd
import os
from homeCatPrograms.catProuduct import *



def ValidaDatafinder(homCatobj ):
    mtdValidData = []

    driver_obj = webdriver.Chrome(executable_path="chromedriver.exe")
    driver_obj.set_window_position(-10000, 0)

    for row in homCatobj:
        # print(row["homeurl"],row['cat_url1'])
        if row['cat_url2'] !=None and row['cat_url2'] !=None :

            catlist_url=  []
            catlist_url.append(row['cat_url1'])
            catlist_url.append(row['cat_url2'])
            catlist_url.append(row['cat_url3'])

            prodList1 = product_finder(home_url=row["homeurl"], category_url=row["cat_url3"],driver_var=driver_obj)
            prodList2 = product_finder(home_url=row["homeurl"], category_url=row["cat_url3"],driver_var=driver_obj)
            if prodList1 !=[] and prodList1 !=[]:
                fianlList=prodList1 + prodList2 + catlist_url
                fianlList.insert(0,row['homeurl'])
                finalData={row['clinet_id']:fianlList}
                mtdValidData.append(finalData)
                # print(finalData)

            else:
                fianlList =  prodList2 + catlist_url
                fianlList.insert(0, row['homeurl'])
                finalData = {row['clinet_id']: fianlList}
                mtdValidData.append(finalData)
                # print(finalData)

        else:
            with open("home_cat_output\\notFound.csv", "a", newline="", encoding="UTF-8") as fp:
                writer = csv.writer(fp)
                writer.writerow([row['clinet_id'], row['homeurl']])


    driver_obj.close()

    return mtdValidData


def saveall_urls(mtd_array):
    with open(f"home_cat_output\mtd_all_urls.csv", "a", newline="", encoding="UTF-8") as fp:
        writer = csv.writer(fp)
        writer.writerow(["clientID", "urls"])

    for Data in mtd_array:
        # print(i)

        for clien_name_var, client_urls in Data.items():

            for client_url in client_urls:
                # print(clien_name_var, client_url)
                with open(f"home_cat_output\mtd_all_urls.csv", "a", newline="", encoding="UTF-8") as fp:
                    writer = csv.writer(fp)
                    writer.writerow([clien_name_var, client_url])


def mtdCsvToarray(mtdCsvData):
    mtdDataDictList = []
    for site_id_var in mtdCsvData['clientID'].unique():
        side_column = list(mtdCsvData['urls'].loc[mtdCsvData['clientID'] == site_id_var].values)
        newMtdData = {site_id_var: side_column}
        mtdDataDictList.append(newMtdData)

    return mtdDataDictList
