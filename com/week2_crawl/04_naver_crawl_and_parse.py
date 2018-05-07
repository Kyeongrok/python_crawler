from urllib.request import urlopen
from bs4 import BeautifulSoup

# mac:ctrl + g, window:alt + j
url = "https://www.naver.com/"
html = urlopen(url)


bsObj = BeautifulSoup(html, "html.parser")
atags = bsObj.findAll("a", {"class":"an_a mn_mail"})

ul_an_l = bsObj.find("ul", {"id":"PM_ID_serviceNavi"})

for item in ul_an_l:
    try:
        print(item.find("a").find("span", {"class":"an_txt"}).text)
    except:
        print("", end="")

