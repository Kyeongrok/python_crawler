import requests
from bs4 import BeautifulSoup
from libs.crawler import crawl

url = "http://www.holybible.or.kr/BIBLE_hkjv/"

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    tables = bsObj.findAll("table")
    oldTable = tables[8]
    newTable = tables[11]

    print(newTable)

    oldTk3s = oldTable.findAll("td", {"class":"tk3"})
    newTk3s = newTable.findAll("td", {"class":"tk3"})

    kjvUrl = "http://www.holybible.or.kr/BIBLE_hkjv/"
    for td in newTk3s:
        href = td.find("a")['href']
        print("{}{}".format(kjvUrl, href))


result = parse(crawl(url))