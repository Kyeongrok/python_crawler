# 쿠팡에서 특정 키워드(beer) 상품명과 상품 가격을 수집 해주세요
# 1.crawl - pageString - requests
# 2.parse
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

    # index, for each
    products = []
    for li in lis:
        name = li.find("div", {"class":"name"})
        price = li.find("strong", {"class":"price-value"})
        link = ""
        product = {"name":name.text}
        products.append(product)

    return products

keywordResult = []
for page in range(1, 13 + 1):
    # pageString을 먼저 출력 해주세요.
    url = "https://www.coupang.com/np/search?q=candy&channel=recent&component=&eventCategory=SRP&listSize=72&brand=&rating=0&page={}".format(page)
    pageString = crawl(url)
    products = parse(pageString)
    print(products)
    keywordResult = keywordResult + products
print(len(keywordResult))

