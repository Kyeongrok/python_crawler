import requests
from bs4 import BeautifulSoup
import json
# 쿠팡 특정 키워드로 검색한 첫페이지 데이터 60개 받아오기

# crawl
# parse
# --- 17페이지까지 1000개 수집
# 분석하기 최대, 최소 등
# https://github.com/Kyeongrok/python_crawler
def crawl(pageNo):
    url = "https://www.coupang.com/np/search?component=&q=%EC%83%9D%EC%88%98&channel=user&page={}".format(pageNo)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) 26.109 Safari/537.36"
    }
    data = requests.get(url, headers=headers)
    print(data)
    return data.content

def getProduct(li):
    name = li.find("div", {"class":"name"})
    price = li.find("div", {"class":"price"})
    strong = price.find("strong")
    return {"name":name.text, "price":strong.text.replace(",", "")}

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul", {"id":"productList"})
    lis = ul.findAll("li")
    products = []
    for li in lis:
        product = getProduct(li)
        products.append(product)
    return products

result = []
for pageNo in range(1, 17):
    pageString = crawl(pageNo)
    products = parse(pageString)
    result = result + products
print(len(result))

file = open("./result.json", "w+")
file.write(json.dumps(result))



