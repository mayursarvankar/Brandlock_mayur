import datetime
import platform
import random
import os
import time
import socket
import requests
import  sched

linux_countries = ['al', 'ar', 'au', 'at', 'br', 'bg', 'ca', 'cl', 'cr', 'hr', 'cy', 'cz', 'dk', 'ee', 'fi',
        'fr', 'ge', 'de', 'gr', 'hk', 'hu', 'is', 'in', 'id', 'ie', 'il', 'it', 'jp', 'lv', 'lu', 'my',
        'mx', 'md', 'nl', 'nz', 'mk', 'no', 'pl', 'pt', 'ro', 'rs', 'sg', '', 'si', 'za', 'kr', 'es',
        'se', 'ch', 'tw', 'th', 'tr', 'ua', 'So', 'uk', 'us']

windows_countries = ['United States', 'Canada', 'Argentina', 'Brazil', 'Mexico', 'Costa Rica', 'Chile',
                     'United Kingdom', 'Germany', 'France', 'Netherlands', 'Sweden', 'Switzerland',
                     'Denmark', 'Poland', 'Italy', 'Spain', 'Norway', 'Belgium', 'Ireland', 'Czech Republic',
                     'Austria', 'Portugal', 'Finland', 'Ukraine', 'Romania', 'Serbia', 'Hungary', 'Luxembourg',
                     'Slovakia', 'Bulgaria', 'Latvia', 'Greece', 'Iceland', 'Estonia', 'Albania', 'Croatia',
                     'Cyprus', 'Slovenia', 'Moldova', 'Bosnia and Herzegovina', 'Georgia', 'North Macedonia',
                     'Turkey', 'South Africa', 'India', 'Israel', 'Turkey', 'United Arab Emirates', 'Australia',
                     'Taiwan', 'Singapore', 'Japan', 'Hong Kong', 'New Zealand', 'Malaysia', 'Vietnam', 'Indonesia',
                     'South Korea', 'Thailand']

my_contries=['United States', 'Canada']


# timeout = time.time() + 60*1
#
# while True:
#     time.sleep(10)
#     print(f"after every Minute : {time.time()}")

#

def ip_adrees():
    r=requests.get("https://httpbin.org/ip")
    try:
        IPAddr=r.json()['origin']
    except:
        IPAddr = ""

    return IPAddr


def nordvpn():
        before_ip=ip_adrees()
        print(f"brfore rotating ip {before_ip}")
        os.chdir('C:\\Program Files\\NordVPN')
        # server = "nordvpn -c -g \'" + random.choice(windows_countries) + "\'"
        disconnect= "nordvpn -d"
        os.system(disconnect)
        time.sleep(10)
        # server = "nordvpn -c -g \'" + "Canada" + "\'"
        #
        # os.system(server)

        while True:
            os.system("nordvpn -c -g \'" + random.choice(my_contries) + "\'")
            after_ip=ip_adrees()
            if after_ip != before_ip:
                # before_ip=after_ip
                break


        time.sleep(10)


        print(f"after roted ip {ip_adrees()}")
#

#
# nordvpn()
#
# print(ip_adrees())

def word():
    print("heloo")


# import sched, time
# s = sched.scheduler(time.time, time.sleep)
# def do_something(sc):
#     print("=================================================================")
#     print(f"Doing {datetime.datetime.now()}...")
#     nordvpn()
#     # do your stuff
#     sc.enter(30, 1, do_something, (sc,))
# #
#
# s.enter(30, 1, do_something, (s,))
# s.run()
#
# for i in range(1,10):
#     time.sleep(10)
#     print(i)





# hostname = socket.gethostname()
# local_ip = socket.gethostbyname(hostname)
#
# print(local_ip)