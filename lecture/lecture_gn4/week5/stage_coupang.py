# 만두 한페이지 검색 결과를 크롤링 해보세요
import requests
from bs4 import BeautifulSoup
import json

def crawl(pageNo):
    url = "https://www.coupang.com/np/search?component=&q=만두&channel=user&page={}&listSize=100".format(pageNo)
    data = requests.get(url)
    print(data, url)
    return data.content

def getProduct(li):
    img = li.find("img")
    name = img["alt"]
    strong = li.find("strong", {"class":"price-value"})
    price = strong.text.replace(",", "").replace(",", "")
    aTag = li.find("a")
    href = "https://www.coupang.com" + aTag["href"]
    return {"name":name, "price":price, "link":href}

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul", {"id":"productList"})
    lis = ul.findAll("li")

    products = []
    for li in lis:
        product = getProduct(li)
        products.append(product)
    return products

keywordResults = []
for pageNo in range(1, 10 + 1):
    pageString = crawl(pageNo)
    products = parse(pageString)
    keywordResults += products
print(keywordResults)
print(len(keywordResults))

file = open("./mandoo.json", "w+")
file.write(json.dumps(keywordResults))
