import requests
from bs4 import BeautifulSoup
# crawl함수 - requests
# parse함수 - string -> 원하는 정보
# crawl함수를 만들어 보세요 url -> pageString

def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    noToday = bsObj.find("p", {"class":"no_today"})
    blind = noToday.find("span", {"class":"blind"})

    wrapCompany = bsObj.find("div", {"class":"wrap_company"})
    aTag = wrapCompany.find("a")
    name = aTag.text

    return {"price":blind.text, "name":name}

url = "https://finance.naver.com/item/main.nhn?code=102940"
info = parse(crawl(url))
print(info)

