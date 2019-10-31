import requests
from bs4 import BeautifulSoup

def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content

def getStockInfo(tr):
    tds = tr.findAll("td")
    rank = tds[0].text
    aTag = tds[1].find("a")
    href = aTag["href"]
    name = aTag.text
    nowPrice = tds[2].text
    totalPrice = tds[6].text
    volume = tds[9].text
    return {"rank":rank, "name":name, "href":href, "code":href[20:],
            "nowPrice":nowPrice, "totalPrice":totalPrice, "volume":volume}

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    box_type_l = bsObj.find("div", {"class":"box_type_l"})
    type_2 = box_type_l.find("table",{"class":"type_2"})
    tbody = type_2.find("tbody")
    trs = tbody.findAll("tr")
    stockInfos = []
    for tr in trs:
        try:
            stockInfo = getStockInfo(tr)
            stockInfos.append(stockInfo)
        except Exception as e:
            print("error")
            pass
    return stockInfos


def getSiseMarketSum(sosok, page):
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok={}&page={}".format(sosok, page)
    pageString = crawl(url)
    list = parse(pageString)
    return list

result = []

for page in range(1, 10 + 1): # 500 = 50 * 10
    list = getSiseMarketSum(0, page) #0 코스피 1코스닥
    result += list
print(result)

import json
file = open("./kospi.json", "w+")
file.write(json.dumps(result))
