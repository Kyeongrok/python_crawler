import requests
from bs4 import BeautifulSoup

url = "http://jolse.com/category/tonermist/43/"
result = requests.get(url)

bs_obj = BeautifulSoup(result.content, "html.parser")

box = bs_obj.find("div", {"class":"box"}) # 가장 처음 나오는걸 return
print(box)