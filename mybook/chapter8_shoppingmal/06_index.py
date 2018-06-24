import requests
import bs4

url = "http://jolse.com/category/tonermist/43/"
result = requests.get(url)

bs_obj = bs4.BeautifulSoup(result.content, "html.parser")

ul = bs_obj.find("ul", {"class":"prdList column5"})

boxes = ul.findAll("div", {"class":"box"})

def get_proudct_info(box):
    ptag = box.find("p", {"class": "name"})
    spans = ptag.findAll("span")
    return spans[1].text

for box in boxes:
    product_info = get_proudct_info(box)
    print(product_info)

