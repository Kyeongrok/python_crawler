from libs.crawler import crawl
from bs4 import BeautifulSoup

import re
pattern = 'CI=[0-9]{3,4}'
pattern = re.compile(pattern)

def parse(pageString, pageTableIndex):
    bsObj = BeautifulSoup(pageString, "html.parser")
    tables = bsObj.findAll("table")
    pageTable = tables[pageTableIndex]
    aTags = pageTable.findAll("a")

    tkbs = bsObj.findAll("td", {"class":"tkb"})
    bookName = tkbs[1].find("b").text.split(" ")[0]

    if(len(aTags) != 0):
        lastPageATag = aTags[len(aTags) - 2]
        lastHref = lastPageATag['href']
        findAll = pattern.findall(lastHref)
        lastCi = int(findAll[0].replace("CI=", ""))
        totalPage = int(lastPageATag.text)
        firstCi = lastCi - totalPage + 1

        return {"bookName":bookName, "firstCi":firstCi, "lastCi":lastCi, "totalPage":totalPage}
    else:
        return {"bookName":bookName, "totalPage":1}


# 책 번호 1~66
def getBookInfo(versionCode):
    bookInfo = []
    for vl in range(1, 67):
        url = "http://www.holybible.or.kr/{}/cgi/bibleftxt.php?VR=0&VL={}&CN=1&CV=99&FR=".format(versionCode, vl)
        pageString = crawl(url)
        try:
            # kjv는 7, b_gae는 8
            result = parse(pageString, 8)
            result['versionCode'] = versionCode
            if(result['totalPage'] != 1):
                pass
            else:
                result['url'] = url
            bookInfo.append(result)
            print(result)
        except Exception as e:
            print("--error--", e)
    return bookInfo

versionCode = "B_GAE"
bookInfo = getBookInfo(versionCode)
import json
file = open("{}_book_info.json".format(versionCode), "w+")
file.write(json.dumps(bookInfo))
