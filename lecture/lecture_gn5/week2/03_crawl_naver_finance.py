import requests # 크롤링 하는 라이브러리
from bs4 import BeautifulSoup # 파싱하는 라이브러리
# 크롤 크롤링 crawl crawling - url로 페이지 문자열(data)을 받아오는 것
# 파스 파싱 parse parsing - 문자열(data)에서 필요한 정보(info)만 뽑아내는 것
# 017800, 000660

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    # tag 태그<다음에 오는 것, class 클래스, id 아이디
    noToday = bsObj.find("p", {"class":"no_today"})
    blind = noToday.find("span", {"class":"blind"})
    wrapCompany = bsObj.find("div", {"class":"wrap_company"})
    aTag = wrapCompany.find("a")
    code = wrapCompany.find("span", {"class":"code"})
    img = wrapCompany.find("img")
    return {"price":blind.text, "name":aTag.text,
            "code":code.text, "kind":img['alt']}

def crawl(code):
    url = "https://finance.naver.com/item/main.nhn?code={}".format(code)
    response = requests.get(url)
    print(response)
    return response.content

codes = ["017800", "000660", "041930"]
for code in codes:
    pageString = crawl(code)
    # result1 = plus(10, 20)
    # result3 = multiple(result1, result2)
    companyInfo = parse(pageString)
    print(companyInfo)

# (10 + 20) * (30 - 40)