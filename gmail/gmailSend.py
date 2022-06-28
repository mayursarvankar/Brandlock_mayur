import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = "mayursarvankar@gmail.com"
EMAIL_PASSWORD = "sapna@4201"

contacts = ['YourAddress@gmail.com', 'test@example.com']

msg = EmailMessage()
msg['Subject'] = 'Check out Bronx as a puppy!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'YourAddress@gmail.com'

with smtplib.SMTP('smtp@gmail.com',993) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # smtp.ehlo()
    # smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    # # body= "how are you"
    # subject ="this is subject"
    #
    # msg=f"Subject :{subject}\n\n{body}"
    #
    # smtp.sendmail(EMAIL_ADDRESS,"mayur@brandlock.io",msg)

