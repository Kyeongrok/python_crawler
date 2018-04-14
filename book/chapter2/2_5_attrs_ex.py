from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

images = bsObj.findAll("img")
print(len(images))

for image in images:
        print(image.attrs['src'])
