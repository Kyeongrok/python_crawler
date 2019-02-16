from bs4 import BeautifulSoup

def getProductInfo(li):
    title = li.find("div", {"class":"info"}).find("a")['title']
    price = li.find("span", {"class":"price"})
    priceReload = price.find("span", {"class":"num _price_reload"})
    info = li.find("div", {"class":"info"})
    href = info.find("a")["href"]
    return {"price":priceReload.text, "title":title, "link":href}

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul", {"class":"goods_list"})
    lis = ul.findAll("li", {"class":"_itemSection"})
    products = []
    for li in lis:
        try:
            productInfo = getProductInfo(li)
            products.append(productInfo)
        except:
            print("----error-----")
    return products