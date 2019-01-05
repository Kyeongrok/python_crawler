from bs4 import BeautifulSoup
def getProduct(li):
    name = li.find("dt").find("img")['alt']
    price = li.find("em", {"class":"sale"}).find("strong").text
    link = li.find("a", {"class":"baby-product-link"})
    return {"name":name, "price":price, "link":link['href']}

def getProducts(string):
    bsObj = BeautifulSoup(string, "html.parser")
    ul = bsObj.find("ul", {"id":"productList"})
    lis = ul.findAll("li")

    products = []
    for li in lis:
        product = getProduct(li)
        products.append(product)
    return products