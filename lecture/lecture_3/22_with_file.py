import requests
from bs4 import BeautifulSoup
import dorm_libs.fileSaver as saver

html = open("./jolse_packpeel_27.html", encoding="utf-8")
print(html)
bs_obj = BeautifulSoup(html, "html.parser")

boxes = bs_obj.findAll("div", {"class":"box"})
def getProductInfo(box):
    aaa = box.find("a").find("img")
    productName = aaa['title']

    lis = box.findAll("li", {"class":"xans-record-"})
    spans = lis[1].findAll("span")
    return spans[1].text

box = boxes[0]
print(getProductInfo(box))
