from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001&date=20180512&page=2"

html = urlopen(url)
bs_obj = BeautifulSoup(html, "html.parser")

lis = bs_obj.find("div", {"class":"list_body newsflash_body"}).findAll("li")

for item in lis:
    print(item)

