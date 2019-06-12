from libs.crawler import crawl
from bs4 import BeautifulSoup
import libs.bibleFinder as finder

url = "http://www.365qt.com/TodaysQT.asp?QTID=7617"
pageString = crawl(url)

def addLine(guideText):
    result = ""
    for i in range(len(guideText)):
        result += guideText[i]
        if(i % 73 == 0):
            result += "\n"
    return result

def parse(pageString):
    result = {}
    bsObj = BeautifulSoup(pageString, "html.parser")
    # print(bsObj)

    qtDayText2 = bsObj.find("div", {"id":"qtDay"})
    try:
        result['qtDayText2'] = qtDayText2.text
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
print(result['qtDayText2'])
print(result['ps4'])
print(result['bx2'])

res = finder.findBetween("민",12,1,8)
for re in res:
    print(re['index'], re['text'])
