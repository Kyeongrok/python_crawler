from libs.coupang.crawler import crawl
from libs.coupang.parser import parse

def getCategory(categoryNo):
    result = []
    for pageNo in range(1, 17 + 1):
        pageString = crawl(categoryNo, pageNo)
        products = parse(pageString)
        result = result + products
    return result

result = getCategory("195297") # 1020
for item in result:
    print(item)
print(len(result))


