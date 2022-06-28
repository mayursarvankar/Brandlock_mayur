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
from  MTD_last.util import *

import os




links=['https://www.flipkart.com/bigstep-very-soft-2-feet-lovable-huggable-happy-birthday-teddy-bear-girlfriend-birthday-gift-boy-girl-49-cm/p/itmc64b520ebefa4?pid=STFG6ASKHXVRGFJM&lid=LSTSTFG6ASKHXVRGFJMEUFSBS&marketplace=FLIPKART&store=tng%2Fclb&srno=b_1_2&otracker=hp_omu_Toys%2Band%2BStationary_3_10.dealCard.OMU_XS7ZM2LSHNYP_5&otracker1=hp_omu_WHITELISTED_neon%2Fmerchandising_Toys%2Band%2BStationary_NA_dealCard_cc_3_NA_view-all_5&fm=neon%2Fmerchandising&iid=en_oU17GEVkaZzP8ph6eQwlegoBOkfwi7kZ66LRCDOQOoNAzdhORxl%2FS9ryIQ8htF60Q1A7R3faBSn2CZtDpy6yXQ%3D%3D&ppt=browse&ppn=browse&ssid=af7xzbvti80000001649150672569',
        'https://www.amazon.com/Zodiac-Baracuda-Automatic-Inground-MX6/dp/B00IG9LZ4C/ref=sr_1_1?crid=31JRL85E2NGET&keywords=Zodiac+MX6+In-Ground+Suction+Si&qid=1649055024&sprefix=zodiac+mx6+in-ground+suction+si%2Caps%2C236&sr=8-1',
           'https://www.currentbody.com/products/dr-harris-anti-wrinkle-sleep-mask?variant=39720558428204',
           'https://www.target.com/p/hershey-39-s-easter-solid-milk-chocolate-eggs-16oz/-/A-84109250#lnk=sametab']

def deal_profile2(urlList):


    driver_var=driverExtenstio("deal_msa")

    Resurllist = []

    for url in urlList:

        driver_var.get(url)

        time.sleep(5)

        set_cookie(drivar_obj=driver_var, cookie_name="_blka_uab", cookie_value="101")
        driver_var.refresh()


        page_is_loading(driver_var)

        # clearing_cookie_button
        try:
            driver_var.find_element(By.XPATH, "//button[contains(.,'Accept')").click()
        except:
            pass

        try:
            driver_var.find_element(By.XPATH, "//button[contains(.,'Allow') ]").click()
        except:
            pass

        try:
            driver_var.find_element(By.XPATH, "//button[contains(text(),'Accept')]").click()
        except:
            pass

        try:
            driver_var.find_element(By.XPATH, "//button[contains(text(),'Allow') ]").click()
        except:
            pass





        time.sleep(1)

        # ===============================removingextrnnsions

        try:
            driver_var.execute_script(''' document.querySelector('iframe[ scrolling="no"]').remove()''' )
            time.sleep(1)
        except:
            pass

        try:
            driver_var.execute_script(''' document.querySelector('iframe[src = "chrome-extension://pbjikboenpfhbbejgkoklgkhjpfogcam/static/html/localProxy.html?ubpSandboxHandle=PComp-UBPNotif_iid%3D-8230230007533049_sid%3D-1171711970393501_time%3D1622466973334&target=https%3A%2F%2Fmatch.amazonbrowserapp.com%2Fxcomp%2Fdesktop%3Ftag%3Damz-mkt-chr-us-20%26ascsubtag%3D1ba00-01000-org00-win10-other-nomod-us000-pcomp-feature-scomp%26u%3Dhttps%253A%252F%252Fwww.amazon.com%26mp%3DUs%26sc%3D%257B%2522content%2522%253A%2522Amazon.com.%2520Spend%2520less.%2520Smile%2520more.%2520%2522%2523%2522contentType%2522%253A%2522SearchQuery%2522%2523%2522scraperType%2522%253A%2522UrlJsRegex%2522%2523%2522scraperSource%2522%253A%2522Alexa%2522%257D%26wt%3DSComp%26co%3Dhttps%253A%252F%252Fwww.google.com%26l%3Den_US%26c%3DUSD%26ubpSandboxHandle%3D1"]').remove()''')

            time.sleep(1)
        except:
            pass

        try:
            driver_var.execute_script(''' document.querySelector('iframe[id *= priceBlinkAds]').remove()''' )
            time.sleep(1)
        except:
            pass



        try:
            # deal_mule_slecot = driver_var.execute_script(By.CSS_SELECTOR,  "iframe[scrolling='no']" or '#msAssistantAds\;' or 'iframe#amznDeals')
            deal_mule_slecot = driver_var.execute_script(''' return (document.querySelector("div[id *='msAssistantAds']")) ''')

            if deal_mule_slecot != None:
                deal_selectors_var= 'msa_present'
                Resurllist.append(deal_selectors_var)
            else:
                deal_selectors_var = 'deal_msa_absent'
                Resurllist.append(deal_selectors_var)
        except:
            deal_selectors_var = 'deal_msa_absent'
            Resurllist.append(deal_selectors_var)

        if deal_selectors_var =='msa_present':break

    result = Resurllist[-1]

    return result, driver_var


# xv=deal_profile2("https://www.tula.com/products/hydrating-day-night-cream?variant=39313319100462")
# print(xv)
# xv=deal_profile2("https://www.amazon.com/")
# print(xv)

# print(deal_profile2(['https://www.tula.com/products/hydrating-day-night-cream?variant=39313319100462']))


