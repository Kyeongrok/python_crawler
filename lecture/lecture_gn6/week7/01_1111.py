import requests
from bs4 import BeautifulSoup

def crawl(url):
    data = requests.get(url)
    print(data, url)
    return data.content

def getProductInfo(li):
    img = li.find("img")
    priceReload = li.find("span", {"class":"_price_reload"})
    info = li.find("div", {"class":"info"})
    link = info.find("a")['href']
    return {"name":img['alt'], "price":priceReload.text, "link":link}

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul", {"class":"goods_list"})
    lis = ul.findAll("li", {"class":"_itemSection"})
    products = []
    for li in lis:
        try:
            products.append(getProductInfo(li))
        except Exception as e:
            print("----error---")
    return products

result = []
def getProducts(pageNo):
    url = "https://search.shopping.naver.com/search/all.nhn?origQuery=%EC%BB%A4%ED%94%BC&pagingIndex={}&pagingSize=40&viewType=list&sort=rel&frm=NVSHPAG&query=%EC%BB%A4%ED%94%BC".format(pageNo)
    pageString = crawl(url)
    products = parse(pageString)
    return products

for pageNo in range(1, 10 + 1):
    result = result + getProducts(pageNo)

print(len(result))