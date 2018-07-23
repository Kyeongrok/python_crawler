import requests
from bs4 import BeautifulSoup

url = "http://jolse.com/category/tonermist/43/"
result = requests.get(url)

bs_obj = BeautifulSoup(result.content, "html.parser")

boxes = bs_obj.findAll("div", {"class":"box"}) # 전체다 []에 넣어줌

for box in boxes[0:1]:
    p_name = box.find("p", {"class":"name"})
    a_tag = p_name.find("a")
    product_name = a_tag['title']
    print(product_name)

