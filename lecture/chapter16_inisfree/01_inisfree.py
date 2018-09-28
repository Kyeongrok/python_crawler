import requests
import bs4

# 제품 정보 추출하기
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

# 페이지에서 제품 정보 추출하기
def get_page_product(url):
    url = url
    result = requests.get(url)
    bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
    list_cons = bs_obj.findAll("div", {"class":"listCon"})
    return [get_product_info(item) for item in list_cons ]

urls = [
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UA&catCd02=&tp=1&pageNo=1&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UA&catCd02=&tp=1&pageNo=2&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UA&catCd02=&tp=1&pageNo=3&sortStr=",
    "http://www.innisfree.com/kr/ko/ProductListSub.do?catCd01=UA&catCd02=&tp=1&pageNo=4&sortStr=",
]

for url in urls:
    items = get_page_product(url)
    for product_info in items:
        result = "{}@{}@{}@http://www.innisfree.com{}".format(product_info['product_name'], product_info['price'], product_info['soldout'], product_info['link'])
        print(result)


