
from libs.crawler import crawl
from bs4 import BeautifulSoup

def parse(pageString):
    soup = BeautifulSoup(pageString, "html.parser")
    print(soup)

url = "http://dart.fss.or.kr/dsab002/search.ax?reportName=%EB%B0%B0%EB%8B%B9&&maxResults=100&&textCrpNm=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90"
pageString = crawl(url)
infos = parse(pageString)
print(infos)



