def parse(bs_obj):
    boxes = bs_obj.findAll("div", {"class":"box"})
    result = []
    for box in boxes:
        try:
            productInfo = getPrductInfo(box)
            result.append(productInfo)
        except:
            print("error")
    return result

def getPrductInfo(box):
    pname = box.find("p", {"class":"name"})
    aaa = pname.find("a")
    lis = box.findAll("li")
    price = lis[1].findAll("span")[1].text
    return {"name":aaa['title'], "price":price}
