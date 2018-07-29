import requests
import bs4

url = "http://jolse.com/category/tonermist/43/"
result = requests.get(url)

bs_obj = bs4.BeautifulSoup(result.content, "html.parser")

ul = bs_obj.find("ul", {"class":"prdList column5"})

boxes = ul.findAll("div", {"class":"box"})

for box in boxes:
    print(box)

