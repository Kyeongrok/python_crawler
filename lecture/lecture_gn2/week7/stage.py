from libs.coupang.crawler import crawl
from libs.coupang.parser import parse
import json

def getCategoryProducts(categoryNo):
    list = []
    for pageNo in range(1, 17+1):
        string = crawl(categoryNo, pageNo)
        products = parse(string)
        list = list + products
    return list

categoryNo = "195006"
result = getCategoryProducts(categoryNo)
print(len(result))

file = open("result.json", "w+")
file.write(json.dumps(result))




