from urllib.parse import quote
import requests
import bs4

endpoint = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?"
serviceKey = "YT3UUv9aN6QqHX4Jcx2S71obvepXOdEyAvuTAQaxEUV7APbXExwpt2iLQRt98JR%2FgtYb1mxCm3NhinhigcPvVw%3D%3D"
Q0 = quote("서울특별시")
Q1 = quote("강남구")
QT = "1"
QN = quote("삼성약국")
ORD = "NAME"
pageNo = "1"
startPage = "1"
numOfRows = "10"
pageSize = "10"

paramset = "serviceKey=" + serviceKey + "&" + "Q0=" + Q0 + "&" +  "Q1=" + Q1 + \
           "&" + "QT=" + QT + "&" + "QN=" + QN + "&" + "ORD=" + ORD + \
           "&" + "pageNo=" + pageNo + "&" + "startPage=" + startPage + "&" + "numOfRows=" + numOfRows +\
           "&" + "pageSize=" + pageSize

url = endpoint + paramset
print("url : " + url)
result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
items = bs_obj.findAll("item")
for item in items:
    tagged_item = item.find("dutyname")
    print(tagged_item.text)
