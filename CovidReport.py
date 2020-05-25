#!/usr/bin/env python
# coding: utf-8

# In[44]:


import os
import requests
import smtplib
EMAIL_ADDRESS = '' #sender-email
EMAIL_PASSWORD = '' #sender-password
body = ""   
URL = "https://api.rootnet.in/covid19-in/stats/latest" #REST-API URL
r = requests.get(url = URL)
coviddata = r.json() #extract data
for i in coviddata['data']['regional']: #iterate over data
    print([i][0]['loc'],":",[i][0]['totalConfirmed'] )
    body = body + str([i][0]['loc'])+" :" + " " + str([i][0]['totalConfirmed']) + "\n"

unoffsummary = coviddata['data']['unofficial-summary'][0]    
print("\nSummary : ","\nTotal :", unoffsummary['total'],"\nRecovered :", unoffsummary['recovered'],"\nDeaths :", unoffsummary['deaths'],"\nActive :",unoffsummary['active'])

body = body + "\nSummary : " + "\nTotal :" + str(unoffsummary['total']) + "\nRecovered :" + str(unoffsummary['recovered']) + "\nDeaths :" + str(unoffsummary['deaths']) + "\nActive :" + str(unoffsummary['active'])

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls() #encrypt traffic
    smtp.ehlo()     #re-verify
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    subject = "Covid19 Daily Report"
    msg = f'Subject : {subject}\n\n{body}'
    smtp.sendmail(EMAIL_ADDRESS, 'recepient_email', msg)
    server.quit()



