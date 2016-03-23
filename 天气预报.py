#coding:utf-8
import os
import time
import json
import urllib.request
import requests
from bs4 import BeautifulSoup

url="http://api.map.baidu.com/telematics/v3/weather?location=%E6%B7%84%E5%8D%9A&output=json&ak=KPGX6sBfBZvz8NlDN5mXDNBF&callback="
url_font="http://api.map.baidu.com/telematics/v3/weather?location="
url_last="&output=json&ak=KPGX6sBfBZvz8NlDN5mXDNBF&callback="
url_xian="http://api.map.baidu.com/telematics/v3/weather?location=%E8%A5%BF%E5%AE%89&output=json&ak=KPGX6sBfBZvz8NlDN5mXDNBF&callback=%22"
def input_city():
    city=input("city:")
    url=url_font+city+url_last
    return url
def gethtml(url):
    page=urllib.request.urlopen(url).read()
    html=page.decode('utf-8')
    return html

if __name__=='__main__':
    #data=gethtml(input_city())
    data=gethtml(url)
    #soup=BeautifulSoup(data,"html.parser")
    js=json.loads(data)
    if js['status']=='success' and js['error']==0:
        print("北京时间：%s"%js['date'])
        print("pm2.5：%s"%js['results'][0]['pm25'])   
        print("天气：%s"%js['results'][0]['weather_data'][0]['weather'])
        print("风力：%s"%js['results'][0]['weather_data'][0]['wind'])
        print("温度：%s"%js['results'][0]['weather_data'][0]['temperature'])
        for i in js['results'][0]['weather_data']:
            print("-----------%s--------------"%i['date'])
            print(i['weather'])
            print(i['wind'])
            print(i['temperature'])
    #time.sleep(10)
    os.system('pause')
