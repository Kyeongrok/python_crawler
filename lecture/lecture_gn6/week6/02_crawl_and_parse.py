import requests
from bs4 import BeautifulSoup

def crawl(url):
    data = requests.get(url)
    return data.content

def getProductInfo(li):
    aTag = li.find("div", {"class":"info"}).find("a")
    title = ""
    try:
        title = aTag['title']
    except:
        print("----")
    link = aTag['href']
    spanPrice = li.find("span", {"class":"price"})
    price = spanPrice.find("em").find("span").text
    return {"title":title, "price":price, "link":link}

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul", {"class":"goods_list"})
    lis = ul.findAll("li", {"class":"_itemSection"})
    infos = []
    for li in lis:
        infos.append(getProductInfo(li))
    return infos

def getProductInfos(pageNo):
    url = "https://search.shopping.naver.com/search/all.nhn?origQuery=%EA%B8%B4%EB%B0%94%EC%A7%80&pagingIndex={}&pagingSize=40&viewType=list&sort=rel&frm=NVSHPAG&query=%EA%B8%B4%EB%B0%94%EC%A7%80".format(pageNo)
    return parse(crawl(url))

result = []
for pageNo in range(1, 10+1):
    result = result + getProductInfos(pageNo)
print(len(result))