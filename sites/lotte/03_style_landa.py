import requests
from bs4 import BeautifulSoup
url = "http://goods.ellotte.com/goods-fo/goodsDetail/1200261484?dshopNo=10023"

result = requests.get(url)
print(BeautifulSoup(result.content, "html.parser"))
