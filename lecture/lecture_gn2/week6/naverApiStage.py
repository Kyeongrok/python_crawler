from libs.naver.apiCrawler2 import getApiResult
import json
import pandas as pd
# 1. 키워드 -> string -> json()
# 2. string -> [{}, {}]
# 3. [{}, {}] -> file with pandas

result = getApiResult("강남역 만두")
items = result
print("=>", len(items), items[0])

file = open("./naverKeywordResult.json", "w+")
file.write(json.dumps(items))

df = pd.read_json("./naverKeywordResult.json")
writer = pd.ExcelWriter("./naverOutput.xlsx")
df.to_excel(writer, "sheet1")
writer.save()





