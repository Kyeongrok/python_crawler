from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

# 속성의 개수가 2개인 것
tags = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
print(len(tags))
for tag in tags:
    print(tag)
