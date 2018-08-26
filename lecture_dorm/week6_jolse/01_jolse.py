import requests
from bs4 import BeautifulSoup

def get_bs_obj(url):
    result = requests.get(url)
    return BeautifulSoup(result.content, "html.parser")

def get_product_info(box):
    name = box.find("p", {"class":"name"}).find("a")['title']
    xans_record = box.findAll("li", {"class": " xans-record-"})
    org_price = xans_record[0].findAll("span")[1].text
    sales_price = xans_record[1].findAll("span")[1].text
    return {"name":name, "org_price":org_price, "sales_price":sales_price}

url = "http://jolse.com/category/eyeliner/69/"
bs_obj = get_bs_obj(url)
boxes = bs_obj.findAll("div", {"class":"box"})

for box in boxes:
    try:
        print(get_product_info(box))
    except:
        print("unknown error")

