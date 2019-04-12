'''
url이 어떤지 파악하는 용도임
url파악 되었으면
02_parse_book_info를 먼저 봐도 됨
'''
import requests
from bs4 import BeautifulSoup
from libs.crawler import crawl
from libs.jsonFileSaver import save

url = "http://www.holybible.or.kr/BIBLE_hkjv/"
url = "http://www.holybible.or.kr/B_GAE/"

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    tables = bsObj.findAll("table")
    oldTable = tables[8]
    newTable = tables[11]


    oldTk3s = oldTable.findAll("td", {"class":"tk3"})
    newTk3s = newTable.findAll("td", {"class":"tk3"})

    for td in newTk3s:
        href = td.find("a")['href']
        print("{}{}".format(url, href))


result = parse(crawl(url))
print(result)

save(result, "개혁개정url.json")

