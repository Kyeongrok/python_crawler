import requests
from bs4 import BeautifulSoup
import dorm_libs.fileSaver as saver

url = "http://jolse.com/category/tonermist/43/"
result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")

box = bs_obj.find("div", {"class":"box"})
aaa = box.find("a").find("img")
productName = aaa['title']

ppp = box.find("p", {"class":"name"})
# saver.save("./hello.html", productName)
print(productName)

