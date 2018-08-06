import urllib.request
import requests
from bs4 import BeautifulSoup
import html5lib

url = 'http://m.ppomppu.co.kr/new/bbs_view.php?id=tour&no=89857&page=1'
html = urllib.request.urlopen(url)
result = requests.get(url)

bs_obj = BeautifulSoup(result.content, "html5lib")

info = bs_obj.find("div", {"class":"info"})
print(info)

