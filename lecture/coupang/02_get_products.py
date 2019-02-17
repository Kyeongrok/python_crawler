from libs.crawler import crawl
from bs4 import BeautifulSoup

def getProducts(string):
    bsObj = BeautifulSoup(string, "html.parser")

    ul = bsObj.find("ul", {"id":"productList"})
    lis = ul.findAll("li")
    li = lis[1]
    print(li)
    return []


url = "https://www.coupang.com/np/categories/186764?page=1"
pageString = crawl(url)
print(getProducts(pageString))



