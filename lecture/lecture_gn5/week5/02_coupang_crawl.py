# 쿠팡에서 특정 키워드 검색 결과를 name, price, link 1000건 이상 수집해보세요.
# ex) 바디워시
import requests
from bs4 import BeautifulSoup

def crawl(url):
    data = requests.get(url)
    print(data, url)
    return data.content

def getProductInfo(li):
    name = li.find("div", {"class":"name"})
    price = li.find("strong", {"class":"price-value"})
    link =  li.find("a")['href']
    link =  "https://www.coupang.com" + link
    return {"name":name.text, "price":price.text.replace(",",""), "link":link}

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul", {"id":"productList"})
    lis = ul.findAll("li")
    products = []
    for li in lis:
        product = getProductInfo(li)
        products.append(product)
    return products

keywordResult = []
for page in range(1, 14 + 1):
    url = "https://www.coupang.com/np/search?component=&q=%EB%B0%94%EB%94%94%EC%9B%8C%EC%8B%9C&channel=user&listSize=72&page={}".format(page)
    pageString = crawl(url)
    products = parse(pageString)
    keywordResult = keywordResult + products
print(len(keywordResult))

import json
file = open("bodywash.json", "w+")
file.write(json.dumps(keywordResult))
