# 함수 function crawl하는 함수를 만들어 보세요
# 이름crawl -> url을 받아서 pageString return
# parse(pageString) -> list []

import requests
from bs4 import BeautifulSoup

def crawl(url):
    data = requests.get(url)
    print(data, url)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")

    # bsObj에서 상품 정보'들'을 뽑는 기능

    ul = bsObj.find("ul", {"class":"goods_list"})
    lis = ul.findAll("li", {"class":"_itemSection"})
    print(len(lis))
    print(lis[0])
    # 첫번째 제품의 이름을 출력 해보세요

    return []


url = "https://search.shopping.naver.com/search/all.nhn?query=%08%EC%97%90%EC%96%B4%EC%BB%A8&cat_id=&frm=NVSHATC"
pageString = crawl(url)
productInfos = parse(pageString)

print(productInfos)


