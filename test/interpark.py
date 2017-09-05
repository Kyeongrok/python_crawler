from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.ticketlink.co.kr/concert/getConcertList?page=1&categoryId=14&frontExposureYn=Y")
bsObj = BeautifulSoup(html.read(), "html.parser")

print(bsObj)