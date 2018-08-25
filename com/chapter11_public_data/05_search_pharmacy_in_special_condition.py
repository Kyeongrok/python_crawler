from urllib.parse import quote
import requests
import bs4

endpoint = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?"
serviceKey = "YT3UUv9aN6QqHX4Jcx2S71obvepXOdEyAvuTAQaxEUV7APbXExwpt2iLQRt98JR%2FgtYb1mxCm3NhinhigcPvVw%3D%3D"
Q0 = quote("서울특별시")
ORD = "NAME"
pageNo = "1"
startPage = "1"
numOfRows = "5000"

paramset = "serviceKey=" + serviceKey + "&" + "Q0=" + Q0 + "&" + "ORD=" + ORD + \
           "&" + "pageNo=" + pageNo + "&" + "startPage=" + startPage + "&" + "numOfRows=" + numOfRows

url = endpoint + paramset
result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
items = bs_obj.findAll("item")

count = 0
for item in items:
    tagged_item = item.find("dutytime1c")
    if (tagged_item != None):
        close_time = int(tagged_item.text)
        if(close_time > 2100):
            count += 1

print("월요일 9시 이후까지 하는 약국의 수 : " + str(count))
