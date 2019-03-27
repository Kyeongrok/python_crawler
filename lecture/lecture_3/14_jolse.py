import requests
from bs4 import BeautifulSoup

url = "http://jolse.com/category/tonermist/43/"
result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")

box = bs_obj.find("div", {"class":"box"})
aaa = box.find("a").find("img")
productName = aaa['title']

ppp = box.find("p", {"class":"name"})
# saver.save("./1.html", productName)
print(productName)

