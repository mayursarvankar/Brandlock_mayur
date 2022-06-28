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



import time #Import Time
# Point(x=1731, y=69)


with open("kon_smi_op\Simlar_total_visit.csv","a",newline="",encoding="UTF-8") as fp:
   writer=csv.writer(fp)
   writer.writerow(["Sr No","Url","Total_Visit","Date_time","simlar_url"])

df=pd.read_csv(r'kon_smi_op\RMN+Knoji (Duplicates removed).csv')
# print(df.columns)


options = webdriver.ChromeOptions()
options.add_argument('--profile-directory=Profile 5')

# options.add_argument('--disable-browser-side-navigation')

options.add_argument("user-data-dir=C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\User Data")  # Path to your chrome profile

driver_obj = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
driver_obj.maximize_window()





def take_full_screenshot(saving_path):
        myScreenshot = pyautogui.screenshot()
        return myScreenshot.save(str(saving_path))

url_no=0
# for url,web_id in zip(df['Web_url'].values,df['Sr_No'].values):
for url,web_id in zip(['cariuma.com'],['22323']):

            simlar_url = f'https://www.similarweb.com/website/{url}/#overview'
            if url_no == 10:
                break




            url_no = url_no + 1

            # create_folder_ss
            # path_dir = r"C:\Users\Admin\PycharmProjects\db_conection_screenshot\knoji_smilarweb\kon_smi_op\screenshot"
            # if not os.path.exists(str(url_no)):
            #         os.mkdir(os.path.join(path_dir, str(url_no)))

            simlar_ext_url = 'https://www.' + url
            # print(simlar_url)

            # driver_obj.set_page_load_timeout(120)

            # print(simlar_ext_url)

            try:
                driver_obj.get(simlar_ext_url)
            except Exception as ex:
                print(f'error -> {ex}')
                pass

            # time.sleep(60)

            # timeout = time.time() + 60 * 1  # 5 minutes from now
            #
            # while True:
            #     if time.time()>timeout:
            #         break


            # driver_obj.execute_script(f'''alert("page_no : - {url_no}")''')
            # while True:
            #     time.sleep(5)
            #     page_load_status=driver_obj.execute_script('return document.readyState')
            #     print("---------------------------------------------------------------------------------------------------")
            #     print(f'page_load_status : {page_load_status}')
            #
            #     if page_load_status ==  'complete':
            #         break
            #     else:
            #         driver_obj.refresh()
            
            time.sleep(10)





            try:
                cureent_url =driver_obj.current_url
                domain_name = (tldextract.extract(cureent_url)).domain

                saving_ss=r"C:\Users\Admin\PycharmProjects\db_conection_screenshot\knoji_smilarweb\kon_smi_op\screenshot"

                pyautogui.click(x=1731, y=69)
                time.sleep(3)
                clipboard.copy("Non.e")
                pyautogui.click(x=1811, y=546)
                # take_full_screenshot(saving_path=saving_ss + "\\" + str(url_no) + '\\' + domain_name + "_" + "img1.png")
                pyautogui.scroll(-150)
                time.sleep(2)
                pyautogui.click(x=1820, y=905)
                pyautogui.click(x=1820, y=905)
                take_full_screenshot(saving_path=saving_ss + "\\" + str(web_id) + '_' + domain_name + "_" + "img.png")
                # take_full_screenshot(saving_path=)

                pyautogui.hotkey('ctrl', 'c')
                time.sleep(2)
                rest = str(pyperclip.paste())

                # print(rest)

                rest = rest.split('.')
                try:
                    total_vist = rest[0] + '.' + rest[1].replace("0M", "M").replace("0K","K")
                except:
                    total_vist=str(rest) + "_none"

                # print(total_vist)

                dat_time = str(datetime.datetime.now()).split('.')[0]
                # time.sleep(6000)










                print(f'{url_no} --> {url} --> {total_vist} --> {dat_time} --> {simlar_url}')

                with open("kon_smi_op\Simlar_total_visit.csv", "a", newline="", encoding="UTF-8") as fp:
                        writer = csv.writer(fp)
                        writer.writerow([url_no, url, total_vist, dat_time ,simlar_url])
            except:
                with open("kon_smi_op\Simlar_total_visit.csv", "a", newline="", encoding="UTF-8") as fp:
                    writer = csv.writer(fp)
                    writer.writerow([url_no, url, "Error", "Error", "Error"])
    # driver_obj.get('https://fashionnova.com')

# Point(x=1802, y=905)
# time.sleep(60000)

driver_obj.quit()

# sending whatsap mesag===============================================================
last_df=pd.read_csv(r'C:\Users\Admin\PycharmProjects\db_conection_screenshot\knoji_smilarweb\kon_smi_op\Simlar_total_visit.csv')
all_records=last_df.shape[0]
corrrecct_reccord=len([i for i in last_df['Total_Visit'] if "M" in str(i) or  "K" in str(i)])
what_send=f"Out of {all_records} records --> {corrrecct_reccord} <-- are correct"
print(what_send)

#
# hour = datetime.datetime.now().hour
# minute      = datetime.datetime.now().minute
# #1)
# pwat.sendwhatmsg("+918104406233",what_send,hour,minute+2)
# time.sleep(10)
# pyautogui.click(x=1874, y=987)