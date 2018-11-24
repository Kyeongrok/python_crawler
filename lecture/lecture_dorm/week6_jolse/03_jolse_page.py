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

urls = [
    "http://jolse.com/category/eyecare/47/?page=1",
    "http://jolse.com/category/eyecare/47/?page=2",
    "http://jolse.com/category/eyecare/47/?page=3"
]

for url in urls:
    page1_products = get_product_list(url)
    for product in page1_products:
        try:
            print(product['name'] +"@"+ product['org_price'])
        except:
            print("")
