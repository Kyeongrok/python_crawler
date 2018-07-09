import requests
from bs4 import BeautifulSoup

url = "http://jolse.com/category/tonermist/43/"
result = requests.get(url)

bs_obj = BeautifulSoup(result.content, "html.parser")

boxes = bs_obj.findAll("div", {"class":"box"}) # 전체다 []에 넣어줌

for box in boxes:
    print(box)

