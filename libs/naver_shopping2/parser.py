from bs4 import BeautifulSoup

def getProductInfo(li):
    print(li)
    return {}

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul", {"class":"goods_list"})
    lis = ul.findAll("li", {"class":"_itemSection"})

    products = []
    for li in lis:
        product = getProductInfo(li)
        products.append(product)

    return products

