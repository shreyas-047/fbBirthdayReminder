fbBirthdayReminder
==================
This is a simple python script which uses [Facebook Python SDK](https://github.com/pythonforfacebook/facebook-sdk) to retrieve birthdays from facebook's ```user``` and ```friend``` tables. [Twilio-python](https://github.com/twilio/twilio-python) is used to handle text messaging.
To install Facebook Python SDK:
`pip install facebook-sdk`
To install Twilio-python:
`pip install twilio`

Making code ready
==================
#####Prepare GraphAPI object with your Access token.

```python
 gp=GraphAPI("xxxx")
 ```
 You can get access token from [Graph API Explorer](https://developers.facebook.com/tools/explorer). Make sure you select proper permissions to access friends' birthdays.
 
---
#####Set your Twilio credentials.
```python
twilioNumber="xxxx" #Your twilio number
sendTo="xxxx" #phone Number you want recieve texts on
accountSid="xxxx" #Your Twilio account Sid
authToken="xxxx" #Your Twilio account auth token
```
Periodic execution
========================
There two ways you can execute this script on a periodic basis:
#####1. Use [Pythonanywhere](https://www.pythonanywhere.com/)
Pythonanywhere provides 500MB of space for a free account. It allows you to schedule several tasks to run at a partiular time on a daily basis. You can simply use python script `.py` file and bash script `.sh` file as well.
#####2.Use `crontab` in linux
It is very easy to add an entry in `crontab`. Hit `crontab -e` and add a single line at the end of the table.
For example:
`6 15 * * * /Path to./fbRem.sh` means _execute fbRem.sh daily at 15:06_. (It is quite obvious that your system should be ON).
