from libs.ncbi import ncbi_crawler as crawler
import threading
import pandas as pd
import json

df = pd.read_json("./links2.json",dtype={'0':'int64'})
list = []
df.sort_values(by=[0], ascending=False)

def parse(num):
    # print(int(num))
    file = open("/Users/kyeongrok/Desktop/sub_pages2/" + str(int(num)) +".html")
    text = file.read()
    res = crawler.getSubPageContent(text)
    res['id'] = int(num)
    file2 = open("/Users/kyeongrok/Desktop/json_results/"+str(int(num))+".json", "w+")
    file2.write(json.dumps(res))
    file.close()
    file2.close()

for pageNum in df[0]:
    # time.sleep(0.001)
    print(pageNum)
    threading.Thread(target=parse, args=(int(pageNum), )).start()
