# crawl
# parse
# paging
import requests
from bs4 import BeautifulSoup

def crawl(url):
    data = requests.get(url)
    print(data, url)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul", {"id":"productList"})
    lis = ul.findAll("li")
    products = []
    for li in lis:
        # li = lis[0]
        # li = lis[1]
        name = li.find("div", {"class":"name"}).text
        price = li.find("strong", {"class":"price-value"})
        product = {"name":name, "price":price.text}
        products.append(product)
    return products

keywordResult = []
for page in range(1, 11):
    url = "https://www.coupang.com/np/search?q=candy&trcid=&traid=&minPrice=&maxPrice=&priceRange=&filterType=&listSize=72&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}".format(page)
    pageString = crawl(url)
    products = parse(pageString)
    keywordResult = keywordResult + products

print(len(keywordResult))

import json
file = open("./candy.json", "w+")
file.write(json.dumps(keywordResult))

