# 쿠팡에서 마카롱 키워드 검색결과 1000개 수집해서
# 파일로 저장하기

import requests
from bs4 import BeautifulSoup
import json

def crawl(keyword, pageNo):
    #component = 194176
    url = "https://www.coupang.com/np/search?component=194176&q={}&channel=user&page={}".format(keyword, pageNo)
    headers = {'User-Agent': 'Mozilla/5.0'}
    data = requests.get(url, headers=headers)
    print(data, url)
    return data.content

def getProduct(li):
    name = li.find("div", {"class":"name"})
    price = li.find("div", {"class":"price"})
    strong = li.find("strong", {"class":"price-value"})
    return {"name":name.text, "price":strong.text.replace(",","")}

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul", {"id":"productList"})
    lis = ul.findAll("li")
    products = []
    for li in lis:
        product = getProduct(li)
        products.append(product)
    return products

def getKeywordResults(keyword, endPage):
    results = []
    for pageNo in range(1, endPage + 1):
        pageString = crawl(keyword, pageNo)
        products = parse(pageString)
        results = results + products
    return results

