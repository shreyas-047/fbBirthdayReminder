#!/usr/bin/env python
'''
This is a simple python script to fetch upcoming birthdays of your facebook friends and recieve the same on your cell phone via text message. Replace
'''
from facebook import GraphAPI
import datetime
from twilio.rest import TwilioRestClient
import twilio
gp=GraphAPI("xxxx")#replace xxxx with your facebook access token
date1= datetime.date.today() + datetime.timedelta(days=1) # days=2 will retrieve birthdays on the day after tomorrow and so on
date=date1.strftime("%m/%d")
month = date[5:7]
day =date[8:10]
print month , day
query='SELECT name,birthday_date FROM user WHERE uid IN(SELECT uid2 FROM friend WHERE uid1=me()) AND strlen(birthday_date) !=0 AND substr(birthday_date,0,5)="nnnn"'.replace("nnnn",date)
map= gp.fql(query)
if len(map['data']):
    text="Birthdays-%s\n".replace("%s",date)
    for i in range(len(map['data'])):
        text+=str(i+1) +"."+map['data'][i]['name']+" "
else:
    text="No Birthdays!"
twilioNumber="xxxx" #Your twilio number
sendTo="xxxx" #phone Number you want recieve texts on
accountSid="xxxx" #Your Twilio account Sid
authToken="xxxx" #Your Twilio account auth token
try:
    device = TwilioRestClient(accountSid,authToken)
    message = device.sms.messages.create(
        body=text,
        to=sendTo,
        from_=twilioNumber
    )
except twilio.TwilioRestException as e:
    print e
