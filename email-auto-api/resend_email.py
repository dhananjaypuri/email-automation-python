from urllib import response
import requests
import json
import datetime
import pytz

todayDate = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).date();

print(todayDate);

response = requests.get(url=f'http://127.0.0.1:8000/sendmail2/{todayDate}');

print(response.text);