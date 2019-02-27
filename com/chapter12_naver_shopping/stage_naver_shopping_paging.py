import requests
from libs.naver_shopping2.parser import parse
import json

def crawl(pageNo):
    url = "https://search.shopping.naver.com/search/all.nhn?query=텀블러&pagingIndex={}&cat_id=&frm=NVSHATC".format(pageNo)
    data = requests.get(url)
    print(data, url)
    return data.content

totalProducts = []
for pageNo in range(1, 10+1):
    pageString = crawl(pageNo)
    products = parse(pageString)
    totalProducts += products

print(totalProducts)
print(len(totalProducts))


file = open("./tumbler.json", "w+")
file.write(json.dumps(totalProducts))
