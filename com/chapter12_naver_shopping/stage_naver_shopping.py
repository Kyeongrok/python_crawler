from libs.naver_shopping2.crawler import crawl
from libs.naver_shopping2.parser import parse
import json

page_string = crawl('액박+패드')
products = parse(page_string)
print(len(products))

file = open("./products.json", "w+")
file.write(json.dumps(products))