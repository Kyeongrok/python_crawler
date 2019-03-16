# 키워드를 입력하면 검색 total이 몇개인지
# 알려주는 프로그램을 만들어 보세요.
import requests
from bs4 import BeautifulSoup

def crawl(keyword):
    url = "https://www.coupang.com/np/search?q={}&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=2".format(keyword)
    data = requests.get(url)
    print(data)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    searchQueryResult = bsObj.find("div", {"class":"search-query-result"})
    strong = searchQueryResult.findAll("strong")
    total = strong[1].text
    return total.replace(",", "").replace(",","")

def getKeywordTotalCount(keyword):
    pageString = crawl(keyword)
    total = parse(pageString)
    return total

