from bs4 import BeautifulSoup

def getProductInfo(li):
    print(li)
    img = li.find("img")
    alt = img['alt']
    price = li.find("strong", {"class":"basicList_price__2r23_"}).find('span')
    a_tit = li.find("a", {"class":"basicList_link__1MaTN"})
    href = a_tit['href']

    return {"name":alt, "price":price.text.replace(",", ""), "link":href}

def parse(pageString):
    bs_obj = BeautifulSoup(pageString, "html.parser")
    ul = bs_obj.find("ul", {"class":"list_basis"})
    lis = ul.findAll("li", {"class":"basicList_item__2XT81"})

    products = []
    for li in lis:
        try:
            products.append(getProductInfo(li))
        except Exception as e:
            print("--error--", e)

    return products

