import requests
from bs4 import BeautifulSoup

def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content

def getProductInfo(li):

    em = li.find("em", {"class":"_keepCount"})
    print(em)

    return {"zzim":""}


def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul", {"class":"goods_list"})
    lis = ul.findAll("li", {"class":"_itemSection"})

    products = []
    for li in lis[0:10]:
        try:
            product = getProductInfo(li)
            products.append(product)
        except:
            print("--error--")

    return products

page = 2
url = "https://search.shopping.naver.com/search/all.nhn?query=%EC%83%B4%ED%91%B8&cat_id=&frm=NVSHATC&pagingIndex={}".format(page)

pageString = crawl(url)
products = parse(pageString)
print(products)
print(len(products))