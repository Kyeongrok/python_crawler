import requests
from bs4 import BeautifulSoup
# 쿠팡 쇼핑몰의 특정 카테고리를 crawl하는
# function을 만들어보세요
# 카테고리id를 넣으면 string을 return합니다.

def crawl(categoryId):
    url = "https://www.coupang.com/np/categories/{}".format(categoryId)
    data = requests.get(url)
    print(data.status_code, url) # 200, 400, 500
    return data.content

def getProductInfo(li):
    name = li.find("img")['alt']
    priceValue = li.find("strong", {"class":"price-value"}).text
    star = ""
    try:
        star = li.find("em", {"class":"rating"}).text
    except Exception:
        print("error star:", name)

    replyCount = ""

    try:
        replyCount = li.find("span", {"class":"rating-total-count"}).text
    except Exception:
        print("error replyCount:", name)

    return {"name":name, "price":priceValue, "star":star,
            "reply":replyCount.replace("(","").replace(")","")
            }

def parse(string):
    # [{}, {}, {}, {}, {}]
    bsObj = BeautifulSoup(string, "html.parser")
    ul = bsObj.find("ul", {"id":"productList"})
    lis = ul.findAll("li")

    products = []
    for li in lis:
        result = getProductInfo(li)
        products.append(result)

    return products

categoryId = "195435"
string = crawl(categoryId)
products = parse(string)
print(products)