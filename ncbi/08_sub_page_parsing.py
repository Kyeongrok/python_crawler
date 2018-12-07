from libs import ncbi_crawler as crawler
import pandas as pd
import json

df = pd.read_json("./links2.json",dtype={'0':'int64'})
list = []
df.sort_value(by=[0], ascending=False)
for num in df[0]:
    print(int(num))
    file = open("/Users/kyeongrok/Desktop/sub_pages2/" + str(int(num)) +".html")
    text = file.read()
    res = crawler.getSubPageContent(text)
    list.append(res)

file2 = open("./result.json", "w+")
file2.write(json.dumps(list, ensure_ascii=False))
