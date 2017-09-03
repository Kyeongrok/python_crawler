from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

tags = bsObj.findAll("img")
print(len(tags))
for tag in tags:
    print(tag.attrs)
    