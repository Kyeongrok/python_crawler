# crawl이라는 이름의 함수를 만들어 주세요. :string
# requests import해주세요.
# 네이버쇼핑에서 키워드 드럼 세탁기로 검색한 결과를
# 리턴하는 기능을 넣어주세요.

# parse 함수를 만들어 주세요. string을 받아서 :[]


import requests
from bs4 import BeautifulSoup
def crawl(keyword, pageNo):
    url = "https://search.shopping.naver.com/searc" \
          "h/all.nhn?query={}&pagingIndex={}&cat_id=&frm=NVSHATC".format(keyword, pageNo)
    data = requests.get(url)
    print(data.status_code)
    return data.content

def getProduct(li):
    img = li.find("img")
    alt = img['alt']
    price = li.find("span", {"class":"price"})
    imgArea = li.find("div", {"class":"img_area"})
    link = imgArea.find("a", {"class":"img"})
    priceReload = price.find("span", {"class":"_price_reload"})

    return {"name":alt, "price":priceReload.text,
            "link":link['href']}

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul", {"class":"goods_list"})
    lis = ul.findAll("li", {"class":"_itemSection"})
    print(len(lis))

    products = []
    for li in lis:
        try:
            product = getProduct(li)
            products.append(product)
        except:
            print("---error---")
    return products

pageString = crawl("에어컨", 3)
products = parse(pageString)
print("results:", len(products))
print(products)

for product in products[:1]:
    print(product)