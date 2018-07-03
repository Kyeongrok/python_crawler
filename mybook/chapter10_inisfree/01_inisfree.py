import requests
import bs4

url = "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UM&catCd02=&tp=1&pageNo=3&sortStr="
result = requests.get(url)

bs_obj = bs4.BeautifulSoup(result.content, "html.parser")


list_cons = bs_obj.findAll("div", {"class":"listCon"})

def get_product_info(item):
    product_name = item.find("p", {"class":"pdtName"}).find("em").text
    sold_out = item.find("span", {"class":"colorRed"}) or ""
    price = item.find("p", {"class":"price"}).text
    return {"soldout":sold_out, "product_name":product_name, "price":price}

for item in list_cons:
    product_info = get_product_info(item)
    result = "{},{},{}".format(product_info['price'], product_info['soldout'], product_info['product_name'])
    print(result)


