# import 크롤러 url -> string
# import 파서 string -> list[{},{}]
import json
from libs.coupang.coupangCrawler import getString
from libs.coupang.productsParser2 import getProducts

# 기능은 왜 분리 할까요?
# 업무분담
def getCategoryProducts(categoryId, lastPageNum):
    categoryProducts = []
    for pageNum in range(1, lastPageNum+1):
        url = "https://www.coupang.com/np/categories/{}?page={}".format(categoryId, pageNum)
        string = getString(url)
        products = getProducts(string)
        categoryProducts += products
        # categoryProduct = categoryProducts + products
    return categoryProducts

categoryProducts = getCategoryProducts("399742", 17)
print(len(categoryProducts))

file = open("./coupangResults.json", "w+")
file.write(json.dumps(categoryProducts))