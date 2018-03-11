from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://land.naver.com/article/articleList.nhn?rletTypeCd=A01&hscpTypeCd=A01:A03:A04&tradeTypeCd=&cortarNo=1165010700&rletNo=23759&mapLevel=&rltrMbrId=&picId=&sRef=search")
bsObj = BeautifulSoup(html.read(), "html.parser")

nameList = bsObj.findAll("a", {"class":"blue in_view_link"})

sale_list_tbody = bsObj.find("table", {"class":"sale_list _tb_site_img NE=a:cpm"}).find("tbody")
trs = sale_list_tbody.findAll("tr")

for tr in trs:
    title = tr.find("div", {"class":"inner"}).find("span", {"class":"txt"})
    print(title)