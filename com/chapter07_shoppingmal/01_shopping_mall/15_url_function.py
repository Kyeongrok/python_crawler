import requests
import bs4

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
    bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
    ul = bs_obj.find("ul", {"class": "prdList column5"})

    boxes = ul.findAll("div", {"class": "box"})
    product_info_list = [get_proudct_info(box) for box in boxes]

    return product_info_list

url = "http://jolse.com/category/tonermist/43/"
page_products = get_page_products(url)

for page_products in page_products:
    print(page_products)

