from bs4 import BeautifulSoup

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    # 가격을 뽑고 싶을 때 무엇을 알아야 할까요?
    noToday = bsObj.find("p", {"class":"no_today"})
    blind = noToday.find("span", {"class":"blind"})
    wrapCompany = bsObj.find("div", {"class":"wrap_company"})
    name = wrapCompany.find("h2").find("a")
    description = bsObj.find("div", {"class":"description"})
    code = description.find("span")

    return {"price":blind.text, "name":name.text, "code":code.text}

