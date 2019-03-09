import requests
from bs4 import BeautifulSoup
# 쿠팡 특정 키워드로 검색한 첫페이지 데이터 60개 받아오기

# crawl
# parse
# --- 17페이지까지 1000개 수집
# 분석하기 최대, 최소 등
def crawl():
    url = "https://www.coupang.com/np/search?component=&q=%EC%83%9D%EC%88%98&channel=user"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) 26.109 Safari/537.36"
    }
    data = requests.get(url, headers=headers)
    print(data)
    return data.content

def getProduct(li):
    print(li)
    return {}

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul", {"id":"productList"})
    print(ul)
    lis = ul.findAll("li")
    print(len(lis))
    products = []

    return products

pageString = crawl()
products = parse(pageString)
print(len(products))



