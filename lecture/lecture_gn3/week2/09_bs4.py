import requests # 크롤링
from bs4 import BeautifulSoup # 파싱

def crawl(codeNum):
    url = "https://finance.naver.com/item/main.nhn?code={}".format(codeNum)
    data = requests.get(url)
    return data.content

# return을 dictionary로 해보세요.
# 필드(field)는 name, price입니다.
def getCompanyInfo(string):
    bsObj = BeautifulSoup(string, "html.parser")
    wrapCompany = bsObj.find("div", {"class":"wrap_company"})
    atag = wrapCompany.find("a")
    noToday = bsObj.find("p", {"class":"no_today"})
    blind = noToday.find("span", {"class":"blind"})
    return {"name":atag.get_text(), "price":blind.text}

codes = ["000660", "068270", "064350"]
for code in codes:
    print(getCompanyInfo(crawl(code)))
