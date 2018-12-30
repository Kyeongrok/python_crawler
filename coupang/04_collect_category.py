from libs.stringGetter import getPageString
from bs4 import BeautifulSoup
from libs.coupang.productsParser import getProducts

categoryProducts = []
for pageNum in range(1, 18):
    url = "https://www.coupang.com/np/categories/186764?page={}".format(pageNum)
    pageString = getPageString(url)
    products = getProducts(pageString)
    categoryProducts = categoryProducts + products

# 60 * 17 = 600 + 420 = 1000
print(len(categoryProducts))
for product in categoryProducts:
    print(product)