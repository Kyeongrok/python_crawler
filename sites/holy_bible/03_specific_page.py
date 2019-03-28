from libs.crawler import crawl
from bs4 import BeautifulSoup
import json
fileString = open("bookInfo.json").read()
bookInfos = json.loads(fileString)

bookInfo = bookInfos[0]
print(bookInfo)
def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    lis = bsObj.findAll("li")


    tkbs = bsObj.findAll("td", {"class":"tkb"})
    bookName = tkbs[1].find("b").text.split(" ")[0]

    statements = []
    for index in range(len(lis)):
        statement = {"bookName":bookName, "idx":index+1, "text":lis[index].text.replace("\n", "")}
        statements.append(statement)
    return statements

# for index in range(1, bookInfo['totalPage'] + 1 ):
for index in range(1, 2):
    ci = index + bookInfo['firstCi'] - 1

    url = "http://www.holybible.or.kr/BIBLE_hkjv/cgi/bibleftxt.php?VR=0&CI={}&CV=99&FR=H".format(ci)
    result = parse(crawl(url))
    print(result[0])
    print(len(result))

# 훔. 수집을. 또 해보쟈
