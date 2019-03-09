import requests
from bs4 import BeautifulSoup
# 네이버 쇼핑 키워드 에어컨을 검색한 결과 불러오기
def crawl():
    url = "https://search.shopping.naver.com/search/all.nhn?query=에어컨&cat_id=&frm=NVSHATC"
    data = requests.get(url)
    print(data, url)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul", {"class":"goods_list"})
    lis = ul.findAll("li", {"class":"_itemSection"})

    products = []
    for li in lis:
        try:
            img = li.find("img")
            name = img["alt"]
            priceReload = li.find("span", {"class":"_price_reload"})
            price = priceReload.text
            info = li.find("div", {"class":"info"})
            link = info.find("a")["href"]
            product = {"name":name, "price":price, "link":link}
            products.append(product)
        except:
            print("----error----")

    return products

pageString = crawl()
products = parse(pageString)
print("products=>", products)
print("len=>", len(products))