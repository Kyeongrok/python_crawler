from bs4 import BeautifulSoup
from libs.patternMatcher import findMatchedTexts
from libs.bible.bibleAddressGetter import getAddr
from libs.crawler import crawl
from libs.bibleFinder import findBetween

def addLine(guideText):
    result = ""
    for i in range(len(guideText)):
        result += guideText[i]
        if(i % 65 == 0):
            result += "\n"
    return result

def parse(pageString):
    result = {}
    bsObj = BeautifulSoup(pageString, "html.parser")
    # print(bsObj)

    qtDayText2 = bsObj.find("div", {"id":"qtDay"})
    try:
        extDat = findMatchedTexts(qtDayText2.text, "201[\s\S]+")
        ss = extDat[0].split("\r\n        ")
        ss2 = "{} {}".format(ss[0].replace("\n", ". "), ss[1])
        result['date'] = ss2
        res = findMatchedTexts(qtDayText2.text, "\(.+\)")
        result['addr'] = getAddr(res[0])
    except Exception as e:
        print(e)

    box2Content = bsObj.find("div", {"class":"box2Content"})
    result['box2Content'] = box2Content.text

    # result['srcipt'] = script.text

    content = bsObj.find("div", {"id":"content"})
    ps = content.findAll("p")
    result['content']=ps[4].text

    bx2 = bsObj.find("div", {"class":"bx2"})

    guideText = bx2.text
    result['bx2']= addLine(guideText)

    return result

def runDailySam(qtid):
    url = "http://www.365qt.com/TodaysQT.asp?QTID={}".format(qtid)
    pageString = crawl(url)
    result = parse(pageString)

    addr = result['addr']
    print(result['date'], addr)
    statements = findBetween(addr['book'],addr['chapter'],
                      addr['verseFrom'],addr['verseTo'])
    for statement in statements:
        print(statement['index'], statement['text'])
    print(result['content'])
    print(result['bx2'])
    print(result['date'])

