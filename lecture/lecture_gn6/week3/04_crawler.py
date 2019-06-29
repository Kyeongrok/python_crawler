# crawl, parse함수를 만들어 보세요.
# library 라이브러리, module 모듈 -> 누가 미리 만들어 놓은것
import requests
from bs4 import BeautifulSoup # 문자열을 주소로 접근할 수 있게 가공해줍니다
# 무엇을 넣어서 무엇을 나오게(return) 할까?
# crawl함수는 url(주소)을 넣어서 pageSting(data) return
def crawl(url):
    data = requests.get(url)
    print(data, url)
    return data.content

# 무엇을 넣어서 무엇을 리턴(나오게) 합니까?
def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    noToday = bsObj.find("p", {"class":"no_today"}) # noToday
    blind = noToday.find("span", {"class":"blind"})
    price = blind.text
    # 회사 이름도 출력 해보세요.
    wrapCompany = bsObj.find("div", {"class":"wrap_company"})
    aTag = wrapCompany.find("a")
    name = aTag.text
    return {"name":name, "price":price}

# 067630, 000660
def printCompanyInfo(code):
    url = "https://finance.naver.com/item/main.nhn?code={}".format(code)
    pageString = crawl(url)
    companyInfo = parse(pageString)
    print(companyInfo)

printCompanyInfo("055550")
printCompanyInfo("000660")
