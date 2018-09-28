import requests
import bs4

urls = [
    "http://www.innisfree.com/kr/ko/Product.do?catCd01=UM",
    "http://www.innisfree.com/kr/ko/Product.do?catCd01=UA"
]
result = requests.get(urls[0])
bs_obj = bs4.BeautifulSoup(result.content, "html.parser")

div = bs_obj.find("div", {"class":"listStyle1"})
lis = div.findAll("li")


def get_product_info(item):
    price = item.find("p", {"class":"price"})
    name = item.find("p", {"class":"pdtName"}).find("em").text
    return {"name":name, "price":price.text.strip()}

for li in lis:
    product_info = get_product_info(li)
    print("{}@{}".format(product_info['name'], product_info['price']))

