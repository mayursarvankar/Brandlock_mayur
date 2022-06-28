import pyautogui
import pandas as pd
import requests
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
import csv
from pandas.io import clipboard
import pyperclip
import os
import pywhatkit as pwat
from selenium.common.exceptions import TimeoutException
import similarweb
import json

#https://api.similarweb.com/v1/similar-rank/target.com/rank?api_key=20e8efbafed7409bba89bcd9bc5cd508
#https://account.similarweb.com/standard-api
#https://support.similarweb.com/hc/en-us/articles/4414317910929-Website-DigitalRank-API
smilar_api='20e8efbafed7409bba89bcd9bc5cd508'
Headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

domain_name="target.com"
# Parameters
api_url=f"https://api.similarweb.com/v1/similar-rank/{domain_name}/rank?api_key={smilar_api}"
try:
    api_req=requests.get(api_url,headers=Headers)
    print(f'{api_url} --> {api_req.status_code}')

    json_data=json.loads(api_req.text)
    global_rank=json_data['similar_rank']['rank']
except:
    global_rank=""

print(f'{domain_name} --> {global_rank}')
# print(json_data['meta']['request'][''])



