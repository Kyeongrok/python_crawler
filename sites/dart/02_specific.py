from libs.crawler import crawl
from bs4 import BeautifulSoup

url = "http://dart.fss.or.kr/report/viewer.do?rcpNo=20181031800040&dcmNo=6364473&eleId=0&offset=0&length=0&dtd=HTML"

pageString = crawl(url)

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    print(bsObj)

result = parse(pageString)


