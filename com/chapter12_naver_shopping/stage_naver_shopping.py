from libs.naver_shopping2.crawler import crawl
from libs.naver_shopping2.parser import parse

pageString = crawl('')
products = parse(pageString)
print(products)