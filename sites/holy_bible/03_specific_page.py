from libs.crawler import crawl
from bs4 import BeautifulSoup
import json
from libs.jsonFileSaver import save

fileString = open("bookInfo.json").read()
bookInfos = json.loads(fileString)
print(len(bookInfos))
def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")

    lis = bsObj.findAll("li")
    tkbs = bsObj.findAll("td", {"class":"tkb"})
    bookName = tkbs[1].find("b").text.split(" ")[0]
    statements = []
    for index in range(len(lis)):
        text = lis[index].text
        textSplitted = text.split("\n")[0]
        statement = {"bookName":bookName, "idx":index+1, "text":textSplitted}
        statements.append(statement)
    return statements

# for index in range(1, bookInfo['totalPage'] + 1 ):
def getBible(versionCode):
    bible = {}
    for index in range(len(bookInfos)):
        bookInfo = bookInfos[index]
        print(bookInfo)
        ci = index + bookInfo['firstCi']

        vr = "GAE" # kjv:0 b_gae:9
        if(bookInfo['totalPage'] != 1):
            url = "http://www.holybible.or.kr/{}/cgi/bibleftxt.php?VR={}&CI={}&CV=99".format(versionCode, vr, ci)
        else:
            url = bookInfo['url']
        pageString = crawl(url)
        statements = parse(pageString)
        print(len(statements))
        bible[index+1] = statements
    return bible

bible = getBible("B_GAE")
save(bible, "B_GAE_bible.json")

# 훔. 수집을. 또 해보쟈

