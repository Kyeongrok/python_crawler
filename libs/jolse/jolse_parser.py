from bs4 import BeautifulSoup
def getProdInfo(box):
    pName = box.find("p", {"class":"name"})
    aaa = pName.find("a")
    xans = box.findAll("li", {"class":"xans-record-"})
    spans = xans[1].findAll("span")
    price = spans[1].text
    result = {"name":aaa['title'], "price":price}
    return result

def parse(str):
    bs_obj = BeautifulSoup(str, "html.parser")
    boxes = bs_obj.findAll("div", {"class":"box"})
    result = []
    for box in boxes:
        try:
            result.append(getProdInfo(box))
        except:
            print("err")
    return result
