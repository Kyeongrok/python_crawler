'''
110 236 420658
1. http://m.pann.nate.com/ 이 페이지 크롤링 하기
2. data가 들어 있는 tag 찾기
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

url_beauty = "http://m.pann.nate.com/talk/c20012"
html = urlopen(url_beauty)
bsObj = BeautifulSoup(html)

atags = bsObj.find("ul", {"class":"list rank-list"}).findAll("a")

print(len(atags))

for atag in atags:
    print(atags)
