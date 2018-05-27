from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://land.naver.com/article/articleList.nhn?rletTypeCd=A02&tradeTypeCd=&hscpTypeCd=&cortarNo=1168010100&articleOrderCode=&siteOrderCode=&cpId=&mapX=&mapY=&mapLevel=&minPrc=&maxPrc=&minWrrnt=&maxWrrnt=&minLease=&maxLease=&minSpc=&maxSpc=&subDist=&mviDate=&hsehCnt=&rltrId=&mnex=&mHscpNo=&mPtpRange=&mnexOrder=&location=&ptpNo=&bssYm=&schlCd=&cmplYn="

html = urlopen(url)
bs_obj = BeautifulSoup(html, "html.parser")

table = bs_obj.find("table", {"class":"sale_list _tb_site_img NE=a:cpm"})
print(table)