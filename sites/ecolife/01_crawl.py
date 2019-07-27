import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def crawl(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    data = requests.get(url, headers=headers)
    print(data, url)
    return data.content

def getProductInfo(tr):
    tds = tr.findAll("td")
    return {"no":tds[0].text, "name":tds[1].text, "category":tds[2].text,
            "vendor":tds[3].text, "confirmNo":tds[4].text, "licenceNo":tds[5].text
            }

def parser(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    table = bsObj.find("table", {"class":"table table-striped2"})
    tbody = table.find("tbody")

    trs = tbody.findAll("tr")

    productInfos = []
    for tr in trs:
        productInfo = getProductInfo(tr)
        productInfos.append(productInfo)

    return productInfos


def crawlPage(pageNo):
    url = "http://ecolife.me.go.kr/ecolife/sntryAid/index?page={}".format(pageNo)
    pageString = crawl(url)
    products = parser(pageString)
    return products

def save(df, filename):
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer, 'Sheet1')
    writer.save()

result = []
for pageNo in range(1, 164 + 1):
    infos = crawlPage(pageNo)
    print(infos[0])
    result = result + infos

# print(result)
# print(len(result))
#
# df = pd.DataFrame(data=result)
# print(df.count())
# save(df, "./ecolife.xlsx")
