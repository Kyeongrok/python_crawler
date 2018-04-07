from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.naver.com"
html = urlopen(url)

bs_obj = BeautifulSoup(html)

print(bs_obj)

spans = bs_obj.findAll("span", {"class":"an_txt"})

for item in spans:
    print(item)