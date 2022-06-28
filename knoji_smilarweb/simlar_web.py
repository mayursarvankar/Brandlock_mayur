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
import json
import pandas as pd
import re
import csv
import  requests
import random

df=pd.read_csv(r'kon_smi_op\RMN+Knoji (Duplicates removed).csv')

Headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}


with open("kon_smi_op\Simlar_total_visit_June_2022.csv","a",newline="",encoding="UTF-8") as fp:
   writer=csv.writer(fp)
   writer.writerow(["web_id", "url", "api_url", "globaL_rank", "simlar_url", "dat_time"])


apiData={
         "mayursarvankarlink@gmail.com" : "20e8efbafed7409bba89bcd9bc5cd508",
         "mayursarvankar@gmail.com"     : "73036bed44fa4cac96723ad3c651166c",
         "tuteradekh4201@gmail.com"     : "ef9d739263fa41fbbdd412d9081d2df6",
         "teradekhtu42012@gmail.com"    :  "b1db032dd3f04cd1b97d3d26f234e425",
         "mayurbrandlock@gmail"         : "77b6e93f9a6c4e40bad9b53730a4af30"
        }
#

#


def apiFinder(apiInfo,dataPointLimit):

    validApiList = [api for api in apiInfo.values()]
    # validApiList = []
    while True:
        try:
            validApi=random.choice(validApiList)

        except:
            validApi =""

        htiPointUrl = f"https://api.similarweb.com/user-capabilities?api_key={validApi}"
        try :
            htiPointReq=requests.get(htiPointUrl, headers=Headers)
            hitpoint = json.loads(htiPointReq.text)['user_remaining']
        except:
            hitpoint = 0

        # hitpoint = 0

        if hitpoint <=5000 and hitpoint >= dataPointLimit:
            break

        else:
            try:
                validApiList.remove(validApi)
            except:
                break

            # break

        # print(validApiList)

    return validApi,hitpoint







def smililar(minimumDatpointLimt):
    rowNo= 0
    for url, web_id in zip(df['Web_url'].values, df['Sr_No'].values):
        # # for url,web_id in zip(['flipkart.com'],[123]):
        rowNo =rowNo+1

        smilar_api, point = apiFinder(apiInfo=apiData, dataPointLimit=minimumDatpointLimt)

        if smilar_api != "":

            simlar_url = f'https://www.similarweb.com/website/{url}/#overview'
            api_url = f"https://api.similarweb.com/v1/similar-rank/{url}/rank?api_key={smilar_api}"

            # print(simlar_url,api_url)

            try:
                api_req = requests.get(api_url, headers=Headers)
                print("=============================================================")
                print(f'{simlar_url} --> {api_req.status_code}')

                # with open(f"kon_smi_op\screenshot\{web_id}.html", "w", encoding='utf-8') as file:
                #     file.write(api_req.text)

                json_data = json.loads(api_req.text)
                globaL_rank = json_data['similar_rank']['rank']
            except:
                globaL_rank = ""

            dat_time = str(datetime.datetime.now()).split('.')[0]

            print(f'({rowNo}). api url : {api_url} ---> global rank : {globaL_rank} --> {dat_time} ')

            with open("kon_smi_op\Simlar_total_visit_June_2022.csv", "a", newline="", encoding="UTF-8") as fp:
                writer = csv.writer(fp)
                writer.writerow([web_id, url, api_url, globaL_rank, simlar_url, dat_time])

        else:

            print("all api limit has been be finshed ")
            break


# smililar(minimumDatpointLimt=5)


#checkDatapoints
for api in apiData.values():
    htiPointUrl = f"https://api.similarweb.com/user-capabilities?api_key={api}"

    htiPointReq = requests.get(htiPointUrl, headers=Headers)
    hitpoint = json.loads(htiPointReq.text)['user_remaining']


    print(api,hitpoint)