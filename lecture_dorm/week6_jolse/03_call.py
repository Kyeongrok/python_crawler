import urllib.request
import bs4

def get_bs_obj(url):
    html = urllib.request.urlopen(url)
    bs_obj = bs4.BeautifulSoup(html, "html.parser")
    return bs_obj

def get_product(page_number):
    url = "http://jolse.com/category/tonermist/43/?page="
    url = url + page_number
    bs_obj = get_bs_obj(url)

    product_name = bs_obj.findAll("p", {"class":"name"})
    first_name = product_name[0].findAll("span")
    name = first_name[1].text

    org_price = bs_obj.findAll("li", {"class":" xans-record-"})
    first_price = org_price[0].findAll("span")
    original = first_price[1].text

    dis_price = bs_obj.findAll("li", {"class":" xans-record-"})
    first_dis = dis_price[1].findAll("span")
    discount = first_dis[1].text

    return{"product_name":name, "original_price":original, "discount_price":discount}

print(get_product("1"))