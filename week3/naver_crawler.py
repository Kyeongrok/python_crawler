from urllib.request import urlopen
from bs4 import BeautifulSoup

url_beauty = "https://www.naver.com/nvthemecast_body?theme=BEAUTY"
html = urlopen(url_beauty)

# 모래(데이터) -> 반도체 공장(BeautifulSoup bs4)
# 6265 1q2w3e4r
bsObj = BeautifulSoup(html)

atags = bsObj.findAll("a")
print(atags)

# element 요소
# elements 요소들

