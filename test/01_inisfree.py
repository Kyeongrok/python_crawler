import requests
import bs4

def get_product_info(item):
    p_name_obj = item.find("p", {"class":"pdtName"})
    product_name = p_name_obj.find("em").text

    sold_out = item.find("span", {"class":"colorRed"}) or ""
    if sold_out != "":
        sold_out = sold_out.text
        sold_out.replace(" ", "")
    price = item.find("p", {"class":"price"}).text
    price = price.replace('\n', '').replace('\t', '').replace('\r', '').replace("일시품절", "")
    link = p_name_obj.find("a")['href']
    return {"soldout":sold_out, "product_name":product_name, "price":price, "link":link}

def get_page_product(url):
    url = url
    result = requests.get(url)

    bs_obj = bs4.BeautifulSoup(result.content, "html.parser")

    list_cons = bs_obj.findAll("div", {"class":"listCon"})

    return [get_product_info(item) for item in list_cons ]


urls = [
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UA&catCd02=&tp=1&pageNo=1&sortStr=", # UA = 스킨케어 10, UM = 5
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UA&catCd02=&tp=1&pageNo=2&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UA&catCd02=&tp=1&pageNo=3&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UA&catCd02=&tp=1&pageNo=4&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UA&catCd02=&tp=1&pageNo=5&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UA&catCd02=&tp=1&pageNo=6&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UA&catCd02=&tp=1&pageNo=7&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UA&catCd02=&tp=1&pageNo=8&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UA&catCd02=&tp=1&pageNo=9&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UA&catCd02=&tp=1&pageNo=10&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UA&catCd02=&tp=1&pageNo=11&sortStr=",

    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UM&catCd02=&tp=1&pageNo=1&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UM&catCd02=&tp=1&pageNo=2&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UM&catCd02=&tp=1&pageNo=3&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UM&catCd02=&tp=1&pageNo=4&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UM&catCd02=&tp=1&pageNo=5&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UM&catCd02=&tp=1&pageNo=6&sortStr=",

    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UC&catCd02=&tp=1&pageNo=1&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UC&catCd02=&tp=1&pageNo=2&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UC&catCd02=&tp=1&pageNo=3&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UC&catCd02=&tp=1&pageNo=4&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UC&catCd02=&tp=1&pageNo=5&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UC&catCd02=&tp=1&pageNo=6&sortStr=",

    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UN&catCd02=&tp=1&pageNo=1&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UN&catCd02=&tp=1&pageNo=2&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UN&catCd02=&tp=1&pageNo=3&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UN&catCd02=&tp=1&pageNo=4&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UN&catCd02=&tp=1&pageNo=5&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UN&catCd02=&tp=1&pageNo=6&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UN&catCd02=&tp=1&pageNo=7&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UN&catCd02=&tp=1&pageNo=8&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UN&catCd02=&tp=1&pageNo=9&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UN&catCd02=&tp=1&pageNo=10&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UN&catCd02=&tp=1&pageNo=11&sortStr=",

    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UD&catCd02=&tp=1&pageNo=1&sortStr=", # UD 클렌징 5
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UD&catCd02=&tp=1&pageNo=2&sortStr=", # UD 클렌징 5
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UD&catCd02=&tp=1&pageNo=3&sortStr=", # UD 클렌징 5
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UD&catCd02=&tp=1&pageNo=4&sortStr=", # UD 클렌징 5
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UD&catCd02=&tp=1&pageNo=5&sortStr=", # UD 클렌징 5
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UD&catCd02=&tp=1&pageNo=6&sortStr=", # UD 클렌징 5 ctrl+d 한줄복사

    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UF&catCd02=&tp=1&pageNo=1&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UF&catCd02=&tp=1&pageNo=2&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UF&catCd02=&tp=1&pageNo=3&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UF&catCd02=&tp=1&pageNo=4&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UF&catCd02=&tp=1&pageNo=5&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UF&catCd02=&tp=1&pageNo=6&sortStr=",


    ]

for url in urls:
    items = get_page_product(url)
    for product_info in items:
        result = "{}${}${}$http://www.innisfree.com{}".format(product_info['product_name'], product_info['price'], product_info['soldout'], product_info['link'])
        print(result)
