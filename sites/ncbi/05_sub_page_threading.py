import threading
import pandas as pd
import requests
import time

def crawlAndSave(pageNum, ee):
    url = "https://www.ncbi.nlm.nih.gov/pubmed/"+ str(pageNum)
    result = requests.get(url)
    print("url:", url, "status:", result.status_code)
    file2 = open("/Users/kyeongrok/Desktop/sub_pages2/" +str(pageNum) + ".html", "w+", encoding="utf-8")
    str1 = str(result.text)
    file2.write(str(str1))
    file2.close()


df = pd.read_json("./links2.json",dtype={'0':'int64'})

for pageNum in df[0][15412:]:
    time.sleep(0.02)
    threading.Thread(target=crawlAndSave, args=(int(pageNum), "")).start()

