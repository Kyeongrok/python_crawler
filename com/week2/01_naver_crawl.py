from urllib.request import urlopen
from bs4 import BeautifulSoup

# mac:ctrl + g, window:alt + j
url = "https://www.naver.com/"
html = urlopen(url)

# ------- 모래 가지고 오기 ----

bsObj = BeautifulSoup(html, "html.parser")
atags = bsObj.findAll("a", {"class":"an_a mn_mail"})

ul_an_l = bsObj.find("ul", {"class":"an_l"})
lis = ul_an_l.findAll("li")

for li in lis:
    # item에 find를 해서 a tag만 뽑아 보세요

    # li에서 a를 찾아보세요.
    atag = li.find("a")
    print(atag)













