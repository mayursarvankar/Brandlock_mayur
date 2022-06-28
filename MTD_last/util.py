import time
from selenium import webdriver
import os

def set_cookie( drivar_obj, cookie_name, cookie_value):
    try:
        try:
            updated_cok = drivar_obj.get_cookie(cookie_name)
            updated_cok['value'] = cookie_value

            drivar_obj.delete_cookie(cookie_name)

            # print(updated_cok)
            drivar_obj.add_cookie(updated_cok)

        except:
            try:
                drivar_obj.add_cookie({'name': '_blka_uab', 'value': '101'})
            except:
                pass
    except:
        try:
            drivar_obj.add_cookie({'name': '_blka_uab', 'value': '101'})
        except:
            pass


def page_is_loading(driver):
    timeout = time.time() + 60 * 1
    while True:
        try:
            x = driver.execute_script("return document.readyState")

        except:
            x=""
        # print(f"page_status : {x}")


        if x == "complete" or time.time() > timeout :
            break


def chck_link(weblink,home_url):
    if weblink !=None:
        if '.cartier.' not in home_url and 'buy.gazelle' not in home_url and ".luvostore" not in home_url and "geologie."  not in home_url\
                and "invictastores."  not in home_url and '.irestorelaser.' not in home_url and '.kendobrands.'not in home_url:
            if weblink != None and weblink != home_url and weblink.startswith(home_url) \
                    and weblink != home_url and weblink != home_url + "#" and "store" not in weblink.lower() and "careers" not in weblink.lower() and "site" not in weblink.lower() \
                    and "cart" not in weblink.lower() and "log" not in weblink.lower() and "contac" not in weblink.lower() and "Contac" not in weblink.lower() \
                    and "sign" not in weblink.lower() and "brand" not in weblink.lower() and "customer" not in weblink.lower() \
                    and 'wishlist' not in weblink.lower() and 'support' not in weblink.lower() and 'terms' and 'Terms' not in weblink.lower() and 'policy' not in weblink.lower() and 'Policy' not in weblink.lower() \
                    and 'delivery' not in weblink.lower() and 'help' not in weblink.lower() and 'ideas' not in weblink.lower() \
                    and 'faq' not in weblink.lower() and 'about22.90M' not in weblink.lower() and "info" not in weblink.lower() and 'account' not in weblink.lower() and 'program' not in weblink.lower() \
                    and 'sell' not in weblink.lower() and 'repair' not in weblink.lower() and "buy" not in weblink.lower() and 'return' not in weblink.lower() \
                    and 'join' not in weblink.lower() and 'subscription' not in weblink.lower() and "journal" not in weblink.lower() \
                    and 'story' not in weblink.lower() and 'how' not in weblink.lower() and 'try' not in weblink.lower() and '/r/' not in weblink.lower() and 'guide' not in weblink.lower() and "shipping" not in weblink.lower() \
                    and 'people' not in weblink.lower() and "checkout" not in weblink.lower() and "community" not in weblink.lower() and "announcement" not in weblink.lower() \
                    and 'warranty' not in weblink.lower() and 'member' not in weblink.lower() and 'responsibility' not in weblink.lower() and 'terms' not in weblink.lower() and 'accessibility' not in weblink.lower() \
                    and 'education' not in weblink.lower() and 'rewards' not in weblink.lower() and 'reviews' not in weblink.lower() and 'conference'  not in weblink.lower()\
                    and 'outlet' not in weblink.lower() and 'financing' not in weblink.lower() and 'mission' not in weblink.lower()\
                    and 'agreement' not in weblink.lower() and 'filter' not in weblink.lower()and 'agreement' not in weblink.lower()\
                    and "login" not in weblink.lower() and 'promotions' not in weblink.lower() and 'article' not in weblink.lower():
                return weblink
        else:
            return weblink


driverData={"malware":"15",
            "alihunter":"9",
            "deal_amazon":"6",
            "deal_msa":"12",
            "deal_related":"6",
            "msa":"11",
            "similar":"7",
            "stirfy":"10",

            }

def driverExtenstio(extemsion_name):
    options = webdriver.ChromeOptions()  # Path to your chrome profile
    # options.add_argument('--headless')

    options.add_argument(f'--profile-directory=Profile {driverData[extemsion_name]}')
    options.add_argument(
        "user-data-dir=C:\\Users\\Admin\AppData\\Local\\Google\\Chrome\\User Data")  # Path to your chrome profile

    driver_path = os.getcwd().replace("\programs", "")
    driver_obj = webdriver.Chrome(executable_path=f"{driver_path}\chromedriver.exe", options=options)
    driver_obj.maximize_window()
    driver_obj.set_window_position(-10000, 0)

    return driver_obj






