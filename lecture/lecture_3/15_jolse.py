import requests
from bs4 import BeautifulSoup

url = "http://jolse.com/category/tonermist/43/"
result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")

box = bs_obj.find("div", {"class":"box"})
aaa = box.find("a").find("img")
productName = aaa['title']

lis = box.findAll("li", {"class":"xans-record-"})
spans = lis[1].findAll("span")
print(spans[1].text)
