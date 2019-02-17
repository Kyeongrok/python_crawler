import requests
from bs4 import BeautifulSoup

codes = ["000660", "035420"]
def crawl(code):
    url = "https://finance.naver.com/item/main.nhn?code={}".format(code)
    data = requests.get(url)
    string = data.content
    return string

def getCompanyInfo(string):
    bsObj = BeautifulSoup(string, "html.parser")
    wrapCompany = bsObj.find("div", {"class":"wrap_company"})
    name = wrapCompany.find("a").text
    noToday = bsObj.find("p", {"class":"no_today"})
    price = noToday.find("span", {"class":"blind"}).text
    return {"name":name, "price":price}

# 삼성전자, NAVER, SK하이닉스, 셀트리온
for code in codes:
    string = crawl(code)
    result = getCompanyInfo(string)
    print("=>", result)
