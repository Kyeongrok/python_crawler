from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.naver.com/"
html = urlopen(url)


bsObj = BeautifulSoup(html, "html.parser")
atags = bsObj.findAll("a", {"class":"an_a mn_mail"})

ul_an_l = bsObj.find("ul", {"class":"an_l"})
lis = ul_an_l.findAll("li")

for li in lis:
    try:
        atag = li.find("a")
        print(atag)
    except:
        print("", end="")

