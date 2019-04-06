# 쿠팡에서 특정 키워드(에어컨)의 검색결과 첫번째 페이지의
# 첫번째 상품의 이름을 콘솔에 출력 해보세요.
import requests
from bs4 import BeautifulSoup

def crawl(url):
    data = requests.get(url)
    print(data, url)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    dls = bsObj.findAll("dl", {"class":"search-product-wrap"})
    dl = dls[0]
    name = dl.find("div", {"class":"name"})
    strong = dl.find("strong", {"class":"price-value"})
    print(name.text)
    print(strong.text)

    dl = dls[1]
    name = dl.find("div", {"class":"name"})
    strong = dl.find("strong", {"class":"price-value"})
    print(name.text)
    print(strong.text)
    return []

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
pageString = crawl(url)
products = parse(pageString)
print(products)
