import requests
from bs4 import BeautifulSoup
# 쿠팡에서 키워드 카네이션에 대한 모든 데이터 수집 하기
# 수집한 데이터 파일로 저장하기
# name, price, link

def crawl(url):
    # headers = {'User-Agent': 'Mozilla/5.0'}
    data = requests.get(url)
    print(data, url)
    return data.content

def getProductInfo(li):
    name = li.find("div", {"class":"name"}).text
    price = li.find("strong", {"class":"price-value"}).text
    aTag = li.find("a")
    link = "https://www.coupang.com{}".format(aTag['href'])

    return {"name":name, "price":price.replace(",", ""),
            "link":link}

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul", {"id":"productList"})
    lis = ul.findAll("li")
    productInfos = []
    for li in lis:
        productInfo = getProductInfo(li)
        productInfos.append(productInfo)
    return productInfos

keywordResults = []
for page in range(1, 14):
    url = "https://www.coupang.com/np/search?q=생수&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=72&page={}".format(page)
    pageString = crawl(url)
    products = parse(pageString)
    keywordResults = keywordResults + products

import json
file = open("./생수.json", "w+")
file.write(json.dumps(keywordResults))


