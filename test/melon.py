#http://ticket.melon.com/performance/ajax/prodList.json?commCode=&sortType=HIT&perfGenreCode=&perfThemeCode=&filterCode=FILTER_ALL&v=1

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://ticket.melon.com/performance/ajax/prodList.json?commCode=&sortType=HIT&perfGenreCode=&perfThemeCode=&filterCode=FILTER_ALL&v=1")
bsObj = BeautifulSoup(html.read(), "html.parser")

print(bsObj)