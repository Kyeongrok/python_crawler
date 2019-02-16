# 클로러와
# 파서 불러오기
from libs.naver_shopping.crawler import crawl
from libs.naver_shopping.parser import parse

pageString = crawl()
products = parse(pageString)
print(products)
print(len(products))