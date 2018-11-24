import requests
from bs4 import BeautifulSoup

def getBoxes():
    file = open("./jolse_lipliner.html", encoding="utf-8")
    bs_obj = BeautifulSoup(file.read(), "html.parser")
    boxes = bs_obj.findAll("div", {"class":"box"})
    return boxes

def getProductInfo(box):
    p_name = box.find("p", {"class":"name"})
    aaa = p_name.find("a")
    xans_record = box.findAll("li", {"class":" xans-record-"})
    price = xans_record[1].findAll("span")[1].text

    return {"title":aaa['title'], "price":price}

boxes = getBoxes()

for box in boxes[:1]:
    try:
        productInfo = getProductInfo(box)
        print(productInfo)
        message = "{} 상품은 {}입니다.".format(
            productInfo['title'], productInfo['price'])
        print(message)
    except:
        print("error")
