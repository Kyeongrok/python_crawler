from libs.crawler import crawl
from bs4 import BeautifulSoup
import libs.bibleFinder as finder
from libs.patternMatcher import findMatchedTexts
from libs.bible.bibleAddressGetter import getAddr

url = "http://www.365qt.com/TodaysQT.asp?QTID=7618"
pageString = crawl(url)

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
        result['date'] = findMatchedTexts(qtDayText2.text, "201[\s\S]+")
        res = findMatchedTexts(qtDayText2.text, "\(.+\)")
        result['addr'] = getAddr(res[0])
    except Exception as e:
        print(e)

    box2Content = bsObj.find("div", {"class":"box2Content"})
    result['box2Content'] = box2Content.text

    # result['srcipt'] = script.text

    content = bsObj.find("div", {"id":"content"})
    ps = content.findAll("p")
    result['ps4']=ps[4].text

    bx2 = bsObj.find("div", {"class":"bx2"})

    guideText = bx2.text
    result['bx2']= addLine(guideText)

    return result

result = parse(pageString)

addr = result['addr']
print(addr)
res = finder.findBetween(addr['book'],addr['chapter'],
                         addr['verseFrom'],addr['verseTo'])
for re in res:
    print(re['index'], re['text'])
print(result['date'])
print(result['ps4'])
print(result['bx2'])
