from libs.naver_shopping.crawler import crawl
from libs.naver_shopping.parser import parse
from libs.jsonSaver import save

results = []
keywords = ["숨셔바요", "탈취제", "애완동물 냄세"]

for keyword in keywords:
    pageString = crawl(keyword)
    products = parse(pageString)
    results = results + products
print(len(results))

save(results, "./products.json")
# file = open(fileName, "w+")
# file.write(json.dumps(content))
