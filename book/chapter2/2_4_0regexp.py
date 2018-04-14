from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
print(len(images))
for image in images:
        print(type(image.attrs['src']))
        print(image.attrs['src'])
        print(image)
        print(image['src'])
