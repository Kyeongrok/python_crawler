from libs.naver_shopping.crawler import crawl
from libs.naver_shopping.parser import parse

pageString = crawl("숨셔바요")
products = parse(pageString)
print(len(products))
