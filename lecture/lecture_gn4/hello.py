from libs.crawler import crawl
from bs4 import BeautifulSoup

url = "https://search.shopping.naver.com/search/all.nhn?query=%EC%88%A8%EC%85%94%EB%B0%94%EC%9A%94&cat_id=&frm=NVSHATC"
string = crawl(url)
# print(string)

bsObj = BeautifulSoup(string, "html.parser")

print(bsObj)

goodsList = bsObj.find("ul", {"class":"goods_list"})
print(goodsList)