from urllib.request import urlopen
from bs4 import BeautifulSoup

# mac:ctrl + g, window:alt + j
url = "https://www.naver.com/"
html = urlopen(url)

print(html)