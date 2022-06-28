# Import the required modules
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import json
import tldextract
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from datetime import datetime

def page_is_loading(driver_obj):
    timeout = time.time() + 60 * 1
    while True:
        try:
            x = driver_obj.execute_script("return document.readyState")
        except:
            x=""
        # print(f"page_status : {x}")
        if x == "complete" or time.time() > timeout :
            return True
        else:
            yield False

# Main Function
if __name__ == "__main__":

    # Enable Performance Logging of Chrome.

    # driver.set_window_position(-10000, 0)

    with open(f"Taboola_Nomag_Status\Taboola_status.csv","a",newline="",encoding="UTF-8") as fp:
       writer=csv.writer(fp)
       writer.writerow(["Website","Taboola_scripts_url"])

    with open(f"Taboola_Nomag_Status\\Namogoo_status.csv","a",newline="",encoding="UTF-8") as fp:
       writer=csv.writer(fp)
       writer.writerow(["Website","Namogoo_scripts_url"])

    with open(f"Taboola_Nomag_Status\All_status.csv", "a", newline="", encoding="UTF-8") as fp:
        writer = csv.writer(fp)
        writer.writerow(["Website", "Taboola","Namogoo","date_time"])



    # df=pd.read_csv("All-Live-Taboola-Sites.csv")

    df=pd.read_csv("Simlar_total_visit_2022.csv")

    df["globaL_rank"] =df["globaL_rank"].fillna(0)

    df.globaL_rank = df.globaL_rank.astype(int)

    df = df[(df['globaL_rank'] >= 10000) & (df['globaL_rank'] <= 20000)]

    df.to_csv("temp.csv")

    # print(len(df['globaL_rank']))


    # # =====================================================================================

    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities["goog:loggingPrefs"] = {"performance": "ALL"}

    # Create the webdriver object and pass the arguments
    options = webdriver.ChromeOptions()

    # Chrome will start in Headless mode


    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Ignores any certificate errors if there is any
    options.add_argument("--ignore-certificate-errors")

    # Startup the chrome webdriver with executable path and
    # pass the chrome options and desired capabilities as
    # parameters.
    driver = webdriver.Chrome(executable_path="chromedriver.exe",
                              chrome_options=options,
                              desired_capabilities=desired_capabilities)

    driver.maximize_window()
    # driver.set_window_position(-10000, 0)

    compNo=0

    driver.get("https://www.active.com/")

    while not page_is_loading(driver):
        continue

    # websites = ["novica.com", "argos.co.uk","nbcsports.com"]  #

    # # for website in websites:
    # for website in df['Domain'].values:
    #
    # #
    #     website = "https://www." + website
    #
    #
    #     compNo=compNo+1
    #     print(f"================================={compNo}=======================================")
    #
    #     domainName=tldextract.extract(website).domain
    #     # Send a request to the website and let it load
    #
    #     try:
    #         driver.get(website)
    #
    #         while not page_is_loading(driver):
    #             continue
    #
    #         driverVar = True
    #     except Exception as e:
    #         try:
    #             website=website.replace("https://www.","https://")
    #             driver.get(website)
    #
    #             while not page_is_loading(driver):
    #                 continue
    #
    #             driverVar = True
    #         except:
    #
    #
    #             driverVar = False
    #             print(e)
    #             pass
    #
    #     print(website)
    #
    #
    #
    #     all_cooke="//button[contains(text(), 'Accept')]"
    #
    #
    #     # time.sleep(10)
    #     if driverVar:
    #
    #         try:
    #             click_cookie=True
    #             accept_cooki = driver.find_elements(By.XPATH, all_cooke)
    #
    #             # print(accept_cooki[0])
    #
    #             actions = ActionChains(driver)
    #             actions.click(accept_cooki[0]).perform()
    #         except:
    #             click_cookie = False
    #
    #         if not  click_cookie:
    #             try:
    #                 driver.refresh()
    #                 while not page_is_loading(driver):
    #                     continue
    #             except:
    #                 pass
    #
    #
    #
    #
    #         time.sleep(20)
    #
    #         try:
    #             driver.get_screenshot_as_file(f"allScreenshot/{domainName}.png")
    #         except:
    #             pass
    #
    #
    #         # Sleeps for 10 seconds
    #
    #
    #         # Gets all the logs from performance in Chrome
    #         logs = driver.get_log("performance")
    #
    #         # Opens a writable JSON file and writes the logs in it
    #         with open(f"all_network_logs/{domainName}_network_log.json", "w", encoding="utf-8") as f:
    #             f.write("[")
    #
    #             # Iterates every logs and parses it using JSON
    #             for log in logs:
    #                 network_log = json.loads(log["message"])["message"]
    #
    #                 # Checks if the current 'method' key has any
    #                 # Network related value.
    #                 if ("Network.response" in network_log["method"]
    #                         or "Network.request" in network_log["method"]
    #                         or "Network.webSocket" in network_log["method"]):
    #                     # Writes the network log to a JSON file by
    #                     # converting the dictionary to a JSON string
    #                     # using json.dumps().
    #                     f.write(json.dumps(network_log, ensure_ascii=True, indent=4, sort_keys=True) + ",")
    #             f.write("{}]")
    #
    #         # print("Quitting Selenium WebDriver")
    #         # driver.quit()
    #
    #         json_file_path = f"all_network_logs/{domainName}_network_log.json"
    #         with open(json_file_path, "r", encoding="utf-8") as f:
    #             logs = json.loads(f.read())
    #
    #         all_status = {"Taboola": [],
    #                       "Namogoo": []}
    #
    #         # Iterate the logs
    #         for log in logs:
    #
    #             # Except block will be accessed if any of the
    #             # following keys are missing.
    #             try:
    #                 # URL is present inside the following keys
    #                 url = log["params"]["request"]["url"]
    #
    #                 if "taboola" in url:
    #                     print(f'{website} --> {url}')
    #                     all_status["Taboola"].append("present")
    #                     with open(f"Taboola_Nomag_Status\Taboola_status.csv", "a", newline="", encoding="UTF-8") as fp:
    #                         writer = csv.writer(fp)
    #                         writer.writerow([website, url])
    #
    #                 if "cdn.nmgassets.com/TAYVCY680JDL.js" in url or "sitelabweb.com" in url or "mjca-yijws.global.ssl.fastly.net/TAYVCY680_SE.js" in url :
    #                     print(f'{website} --> {url}')
    #                     all_status["Namogoo"].append("present")
    #
    #                     with open(f"Taboola_Nomag_Status\\Namogoo_status.csv", "a", newline="", encoding="UTF-8") as fp:
    #                         writer = csv.writer(fp)
    #                         writer.writerow([website, url])
    #
    #
    #
    #             except Exception as e:
    #                 pass
    #
    #
    #
    #         if len(all_status["Taboola"]) > 0:
    #             all_status["Taboola"]="Present"
    #         else:
    #             all_status["Taboola"]="absent"
    #
    #         if len(all_status["Namogoo"]) > 0:
    #             all_status["Namogoo"]="Present"
    #         else:
    #             all_status["Namogoo"]="absent"
    #
    #         date_time=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    #
    #         with open(f"Taboola_Nomag_Status\All_status.csv", "a", newline="", encoding="UTF-8") as fp:
    #             writer = csv.writer(fp)
    #             writer.writerow([website, all_status["Taboola"], all_status["Namogoo"],date_time])
    #
    #     # print(website)
        # if compNo==2:break


            # driver.quit()