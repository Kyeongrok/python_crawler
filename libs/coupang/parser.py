from bs4 import BeautifulSoup

def getProductInfo(li):
    name = li.find("img")['alt']
    price = li.find("strong", {"class":"price-value"}).text
    return {"name":name, "price":price}

def parse(string):
    bsObj = BeautifulSoup(string, "html.parser")
    ul = bsObj.find("ul", {"id":"productList"})
    lis = ul.findAll("li")
    return [getProductInfo(li) for li in lis]
