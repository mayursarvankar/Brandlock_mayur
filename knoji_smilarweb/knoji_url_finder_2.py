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
import requests
import numpy as np
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import csv

with open("kon_smi_op\knoji_urls.csv","a",newline="",encoding="UTF-8") as fp:
   writer=csv.writer(fp)
   writer.writerow(["Sr_no","Category","Sub-Category","Page No","Url No","Web_url"])

Headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
sr_no=0

Data ={'Apparel' : 'https://knoji.com/brand-directory/fashion/',
        'Beauty'  : 'https://knoji.com/brand-directory/beauty/',
        'Electronics' : 'https://knoji.com/brand-directory/devices/',
        'Health' :'https://knoji.com/brand-directory/health/',
        'Home' : 'https://knoji.com/brand-directory/home/'}

# Data ={'Places & Travel': 'https://knoji.com/brand-directory/places/'}



for category_name,cat_url in  zip(Data.keys(),Data.values()):


        cat_req=requests.get(cat_url,headers=Headers)
        cat_soup=BeautifulSoup(cat_req.text,"lxml")
        sub_urls=cat_soup.select("a.dblock.mb10.ml10",href=True)

        for subcat in sub_urls:
            # if subcat.text =='Travel Services':
                subcat_name=subcat.text
                subcat_url=subcat["href"]

                sub_req = requests.get(subcat_url, headers=Headers)
                sub_soup = BeautifulSoup(sub_req.text, "lxml")

                # ================================================================
                last_page_sele = sub_soup.select("a.pagination_key")

                last_page=[int(i.text) for i in last_page_sele]

                if last_page == []:
                        last_page =[1]


                last_page_no=max(last_page)

               # ================================================================






                brek_page_no = 0

                for i in range(1, int(last_page_no) +1):

                            brek_page_no = brek_page_no + 1
                            # if brek_page_no == 2:
                            #     break

                            subcat_pages_iter = subcat_url + f'?page={i}'
                            subcat_pages_iter_req = requests.get(subcat_pages_iter, headers=Headers)
                            subcat_pages_iter_req_soup = BeautifulSoup(subcat_pages_iter_req.text, "html.parser")

                            web_url_no = 0
                            web_urls = subcat_pages_iter_req_soup.select("td.storedirectory--store >a", href=True)
                            for web_url_one in web_urls:
                                    web_url_no = web_url_no + 1
                                    sr_no = sr_no + 1
                                    web_url = web_url_one['href'].replace('knoji.', '').replace('https://', '')
                                    print(f'{sr_no}. {category_name} --> {subcat_name} --> Page no.{i}--> Url No.{web_url_no} --> {web_url}')

                                    with open("kon_smi_op\knoji_urls.csv", "a", newline="", encoding="UTF-8") as fp:
                                            writer = csv.writer(fp)
                                            writer.writerow(
                                                    [sr_no,category_name, subcat_name, i, web_url_no, web_url])
