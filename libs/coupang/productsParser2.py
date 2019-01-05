from bs4 import BeautifulSoup
def getProduct(li):
    print(li)
    return {"name":"", "price":""}

def getProducts(string):
    bsObj = BeautifulSoup(string, "html.parser")
    ul = bsObj.find("ul", {"id":"productList"})
    lis = ul.findAll("li")
    product = getProduct(lis[0])

    return []