from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

nameList = bsObj.findAll("span", {"class":{"green", "red"}})
print("-----nameList-----")
for name in nameList:
    print(name.get_text())

thePrince = bsObj.findAll(text="the prince")
print("%s" % len(thePrince))
