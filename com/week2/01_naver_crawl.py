from urllib.request import urlopen
from bs4 import BeautifulSoup

# mac:ctrl + g, window:alt + j
url = "https://www.naver.com/"
html = urlopen(url)

# ------- 모래 가지고 오기 ----

bsObj = BeautifulSoup(html)
atags = bsObj.findAll("a", {"class":"an_a mn_mail"})

ul_an_l = bsObj.find("ul", {"class":"an_l"})
lis = ul_an_l.findAll("li")

for item in lis:
    # item에 find를 해서 a tag만 뽑아 보세요
    print(item.find("a"))













