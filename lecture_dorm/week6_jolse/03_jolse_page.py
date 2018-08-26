import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_bs_obj(url):
    html = urlopen(url)
    return BeautifulSoup(html, "html.parser")

def get_product_info(box):
    try:
        name = box.find("p", {"class":"name"}).find("a")['title']
        xans_record = box.findAll("li", {"class": " xans-record-"})
        org_price = xans_record[0].findAll("span")[1].text
        sales_price = xans_record[1].findAll("span")[1].text
        return {"name":name, "org_price":org_price, "sales_price":sales_price}
    except:
        return {}

def get_product_list(url):
    bs_obj = get_bs_obj(url)
    boxes = bs_obj.findAll("div", {"class":"box"})
    return [get_product_info(box) for box in boxes]

    # for box in boxes:
    #     print(get_product_info(box))

url = "http://jolse.com/category/eyecare/47/?page=" + "1"
page1 = get_product_list(url)
print(page1)


