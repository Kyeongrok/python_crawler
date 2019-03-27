import requests
from bs4 import BeautifulSoup

url = "http://jolse.com/category/packpeel/27/"
result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")

print(bs_obj)

boxes = bs_obj.findAll("div", {"class":"box"})
def getProductInfo(box):
    aaa = box.find("a").find("img")
    productName = aaa['title']

    lis = box.findAll("li", {"class":"xans-record-"})
    spans = lis[1].findAll("span")
    return spans[1].text

box = boxes[0]
print(getProductInfo(box))
