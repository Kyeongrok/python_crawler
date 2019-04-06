# 네이버 금융의 특정 종목의 가격을 콘솔에 출력 해보세요.
# pw:careercollege
import requests # 크롤링
from bs4 import BeautifulSoup

def crawl(url):
    data = requests.get(url)
    print(data, url)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    noToday = bsObj.find("p", {"class":"no_today"})
    blind = noToday.find("span", {"class":"blind"})
    wrapCompany = bsObj.find("div", {"class":"wrap_company"})
    h2 = wrapCompany.find("h2")
    aTag = h2.find("a")
    code = wrapCompany.find("span", {"class":"code"})
    return {"price":blind.text, "name":aTag.text, "code":code.text}

codes = ["048410", "000660", "030790"]

companyInfos = []
for code in codes:
    url = "https://finance.naver.com/item/main.nhn?code={}".format(code)
    pageString = crawl(url)
    companyInfo = parse(pageString)
    companyInfos.append(companyInfo)

for company in companyInfos:
    message = "회사 " + company['name'] + "은(는)" + " 현재 가격이 " \
              + company['price'] + "원이고 " + company['code'] +\
              "에 위치해있습니다."
    print(message)