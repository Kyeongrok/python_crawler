import requests # crawl을 하는 module, library, package
# parse를 하는 library도 있습니다. bs4 뷰티풀숩 BeautifulSoup
from bs4 import BeautifulSoup

# crawl이라는 이름의 함수를 만들어 보세요
def crawl(url):
    print("=>", url)
    data = requests.get(url) # ctrl + tab 이전으로가기
    return data.content

def pares(pageString):
    # parsing로직
    bsObj = BeautifulSoup(pageString, "html.parser")
    # 주소 - 페이지상의 주소 -> 페이지상의 주소를 알아내기 -> 개발자도구 chrome
    noToday = bsObj.find("p", {"class":"no_today"})
    blind = noToday.find("span", {"class":"blind"})

    # name에 회사 이름을 찾아서 넣어보세요.
    wrapCompany = bsObj.find("div", {"class":"wrap_company"})
    aTag = wrapCompany.find("a")
    img = wrapCompany.find("img")
    # <img alt="코스닥" />
    # value, property
    code = wrapCompany.find("span", {"class":"code"})
    # dictionary price:얼마, name:무엇
    return {"price":blind.text, "name":aTag.text,
            "category":img['alt'], "code":code.text}

def printCompanyInfo(code):
    url = "https://finance.naver.com/item/main.nhn?code={}".format(code)
    pageString = crawl(url)
    info = pares(pageString)
    print(info)

printCompanyInfo("000660")
printCompanyInfo("005930")
printCompanyInfo("055550")
