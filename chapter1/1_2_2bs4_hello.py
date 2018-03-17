from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.naver.com/")
bsObj = BeautifulSoup(html.read(), "html.parser")

area_navigation = bsObj.find("div", {"class":"area_navigation"})
an_l = area_navigation.find("ul", {"class":"an_l"})
an_items = an_l.findAll("li")
# print(an_items)

for item in an_items:
    an_txt = item.find("span", {"class":"an_txt"})
    print(an_txt.text)