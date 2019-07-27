# ap: dreamtle0919_iptime5g
# pw: 20160919

# 네이버 쇼핑 특정 키워드 검색 결과
# pageString을 받아오는 crawl()과
# [] 로 parsing하는 function을 만들어 주세요.
import requests
from bs4 import BeautifulSoup

def crawl(url):
    data = requests.get(url)
    print(data, url)
    return data.content

def getProductInfo(li):
    # 상품명, 가격, link
    info = li.find("div", {"class":"info"})
    aTag = info.find("a")
    name = ""
    try:
        name = aTag['title']
    except:
        print("here")
        name = aTag.text
    link = aTag['href']
    spanPrice = li.find("span", {"class":"price"})

    # spanPrice => camel case -> java
    # span_price => snake
    # a = 10, b = 20

    price = spanPrice.find("em").find("span", {"class":"num"})

    # a = 10 b = 20 html text -> hyper text <a href="http://"

    return {"name":name, "price":price.text, "link":link}

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul", {"class":"goods_list"})
    lis = ul.findAll("li", {"class":"_itemSection"})

    # parsing 한 data를 return 해주어야 합니다.
    # 44 -> 40개의 상품 정보
    productInfos = []
    for li in lis:
        try:
            productInfo = getProductInfo(li) # {}
            productInfos.append(productInfo)
        except Exception as e:
            print("error:", e)
    return productInfos

# 1~10 page까지 모든 상품 정보를 수집 해보세요.
def getProductInfos(pageNo):
    url = "https://search.shopping.naver.com/search/all.nhn?origQuery=%EA%B8%B4%EB%B0%94%EC%A7%80&pagingIndex={}&pagingSize=40&viewType=list&sort=rel&frm=NVSHPAG&query=%EA%B8%B4%EB%B0%94%EC%A7%80"\
        .format(pageNo)
    pageString = crawl(url)
    infos = parse(pageString)
    return infos # []

result = []
for pageNo in range(1, 3 + 1):
    products = getProductInfos(pageNo)
    result = result + products # [ {}, {}, {}.....{}]
print(result)

print(len(result))

for productInfo in result:
    print(productInfo)

print(len(result))