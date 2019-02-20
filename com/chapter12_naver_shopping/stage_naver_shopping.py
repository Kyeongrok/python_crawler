from libs.naver_shopping2.crawler import crawl
from libs.naver_shopping2.parser import parse
import json

pageString = crawl('')
products = parse(pageString)
print(products)
print(len(products))

file = open("./products.json", "w+")
file.write(json.dumps(products))