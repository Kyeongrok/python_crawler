'''
110 236 420658
1. http://m.pann.nate.com/ 이 페이지 크롤링 하기
2. data가 들어 있는 tag 찾기
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

url_beauty = "http://www.365qt.com/TodaysQT.asp?QTID=6749&WD=1"
html = urlopen(url_beauty)

print(html)
