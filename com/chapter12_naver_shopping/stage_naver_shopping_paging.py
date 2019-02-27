import requests
import pandas as pd
from libs.naver_shopping2.parser import parse
import json

def crawl(pageNo):
    url = "https://search.shopping.naver.com/search/all.nhn?query=텀블러&pagingIndex={}&cat_id=&frm=NVSHATC".format(pageNo)
    data = requests.get(url)
    print(data, url)
    return data.content

keywordTotalProducts = []
for pageNo in range(1, 2):
    pageString = crawl(pageNo)
    products = parse(pageString)
    keywordTotalProducts = keywordTotalProducts + products

for product in keywordTotalProducts:
    print(product)

print(keywordTotalProducts)
print(len(keywordTotalProducts))

df = pd.DataFrame(keywordTotalProducts)
print(df.count())
writer = pd.ExcelWriter("./tumb.xlsx")
df.to_excel(writer, "sheet1")
