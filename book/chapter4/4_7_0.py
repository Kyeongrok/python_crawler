import json
from urllib.request import urlopen
from bs4 import BeautifulSoup

import datetime

html = urlopen("http://www.ticketlink.co.kr/concert/getConcertList?page=1&categoryId=14&frontExposureYn=Y")

ticketJsonString = html.read().decode('utf-8')
ticketJson = json.loads(ticketJsonString)

print(type(ticketJson))

resultList = ticketJson.get("result").get("result")

f = open("새파일.txt", 'w', encoding='utf-8')

print(
    datetime.datetime.fromtimestamp(int("1284101485")).strftime('%Y-%m-%d %H:%M:%S')
)

for item in resultList:
    f.write(item['productName'] + "\n")


f.close()