# crawl함수를 만들어보세요
import requests
from bs4 import BeautifulSoup

def crawl(url):
    data = requests.get(url)
    print(data, url)
    return data.content

def parse(pageString):
    # 상품정보(이름)을 출력하는 parse함수를 만들어보세요.
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul", {"class":"goods_list"})
    lis = ul.findAll("li", {"class":"_itemSection"})
    # list에서 한개 뽑기
    for li in lis:
        try:
            img = li.find("img")
            priceReload = li.find("span", {"class":"num _price_reload"})
            # 가격도 뽑아보세요.
            productInfo = {"name":img['alt'], "price":priceReload.text}
            print(productInfo)
        except Exception as e:
            print("")
    print(len(lis))

url = "https://search.shopping.naver.com/search/all.nhn?query=%EC%9A%B4%EB%8F%99%ED%99%94&cat_id=&frm=NVSHATC"
pageString = crawl(url)
info = parse(pageString)
print(info)

