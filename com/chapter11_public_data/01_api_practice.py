import requests
import bs4

endpoint = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?"
serviceKey = "YT3UUv9aN6QqHX4Jcx2S71obvepXOdEyAvuTAQaxEUV7APbXExwpt2iLQRt98JR%2Fgt" \
             "Yb1mxCm3NhinhigcPvVw%3D%3D"
numOfRows = "10"
pageSize = "1"
pageNo = "1"
MobileOS = "ETC"
MobileApp = "AppTest"
arrange = "A"
contentTypeId = "15"
areaCode = "1"
sigunguCode = "4"
listYN = "Y"

paramset = "serviceKey=" + serviceKey + "&" + "numOfRows=" + numOfRows + "&" +  "pageSize=" + pageSize + \
           "&" + "pageNo=" + pageNo + "&" + "MobileOS=" + MobileOS + "&" + "MobileApp=" + MobileApp + \
           "&" + "arrange=" + arrange + "&" + "contentTypeId=" + contentTypeId + "&" + "areaCode=" + areaCode +\
           "&" + "sigunguCode=" + sigunguCode + "&" + "listYN=" + listYN

url = endpoint + paramset
print(url)
result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
print(bs_obj.findAll("title"))
