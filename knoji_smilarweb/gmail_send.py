# import smtplib
# server=smtplib.SMTP("smtp.gmail.com",587)
# server.ehlo()
# server.starttls()
# server.login("mayursarvankarlink@gmail.com","sapna@4201")
# server.sendmail("mayursarvankarlink@gmail.com","mayursarvankar@gmail.com","hello mayur")
# print("mail sent")
import similarweb

#https://api.similarweb.com/v1/similar-rank/target.com/rank?api_key=20e8efbafed7409bba89bcd9bc5cd508
#https://account.similarweb.com/standard-api
smilar_api='20e8efbafed7409bba89bcd9bc5cd508'

# Parameters
api_key = smilar_api
domain = "similarweb.com"
start_month = "1-2015" # in format M-YYYY
end_month = "2-2015" # in format M-YYYY
time_granularity = "MONTHLY" # Can be: Daily, Weekly, Monthly
main_domain_only = False # get metrics on the main domain only?

#================================
# TrafficAPI
#================================
# client = similarweb.TrafficAPI(api_key, domain, start_month,
#                                end_month, time_granularity,
#                                main_domain_only)
# results = client.query()

#================================
# RankAndReachAPI
#================================
# client = similarweb.RankAndReachAPI(api_key, domain)
# results = client.query()
