import requests
import bs4
import time

def get_proudct_info(box):
    ptag = box.find("p", {"class": "name"})
    spans_name = ptag.findAll("span")
    ul = box.find("ul")
    spans_price = ul.findAll("span")

    name = spans_name[1].text
    price = spans_price[1].text

    atag = box.find("a")
    link = atag['href']

    return {"name":name, "price":price, "link":link}


def get_page_products(url):

    result = requests.get(url)
    time.sleep(2)
    bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
    ul = bs_obj.find("ul", {"class": "prdList column5"})

    boxes = ul.findAll("div", {"class": "box"})
    product_info_list = [get_proudct_info(box) for box in boxes]

    return product_info_list

urls =[
    "http://jolse.com/category/porecare/52/",
    "http://jolse.com/category/peel-off/138/"
]

for page_number in range(0, 2):
    time.sleep(1)
    page_products = get_page_products(urls[page_number])
    print(len(page_products), page_products)

