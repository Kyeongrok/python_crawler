from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup

try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
else:
    bsObj = BeautifulSoup(html.read(), "html.parser")
    print(bsObj.h1)
