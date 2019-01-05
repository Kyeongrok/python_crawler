# import 크롤러 url -> string
# import 파서 string -> list[{},{}]
from libs.coupang.coupangCrawler import getString
from libs.coupang.productsParser2 import getProducts

url = "https://www.coupang.com/np/categories/399742?page=1"
string = getString(url)
products = getProducts(string)
print(products)

