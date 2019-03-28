from libs.crawler import crawl
from bs4 import BeautifulSoup

import re
pattern = 'CI=.{3}'
pattern = re.compile(pattern)

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    tables = bsObj.findAll("table")
    pageTable = tables[7]
    aTags = pageTable.findAll("a")

    tkbs = bsObj.findAll("td", {"class":"tkb"})
    bookName = tkbs[1].find("b").text.split(" ")[0]

    lastPageATag = aTags[len(aTags) - 2]
    lastHref = lastPageATag['href']
    findAll = pattern.findall(lastHref)
    lastCi = int(findAll[0].replace("CI=", ""))
    totalPage = int(lastPageATag.text)
    firstCi = lastCi - totalPage + 1
    return {"bookName":bookName, "firstCi":firstCi, "lastCi":lastCi, "totalPage":totalPage}



# 책 번호 1~66
bookInfo = []
for vl in range(1, 67):
    url = "http://www.holybible.or.kr/BIBLE_hkjv/cgi/bibleftxt.php?VR=0&VL={}&CN=1&CV=99&FR=".format(vl)
    pageString = crawl(url)
    try:
        result = parse(pageString)
        bookInfo.append(result)
        print(result)
    except:
        print("--error--")

import json
file = open("bookInfo.json", "w+")
file.write(json.dumps(bookInfo))
