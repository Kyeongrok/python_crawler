from bs4 import BeautifulSoup

def getCompanyInfo(string):
    bsObj = BeautifulSoup(string, "html.parser")
    wrapCompany = bsObj.find("div", {"class":"wrap_company"})
    # wrapCompany a tag 찾을려면?
    atag = wrapCompany.find("a")
    noToday = bsObj.find("p", {"class":"no_today"})
    blind = noToday.find("span", {"class":"blind"})
    return {"name":atag.text, "price":blind.text}
