from urllib.request import urlopen
import json

url = "http://grains.krei.re.kr/chart/main_chart/index/kind/S/sdate/1999-01-01/edate/2018-05-05"
html = urlopen(url)

json_obj = json.load(html)

for item in json_obj:
    # print(item)
    # date, settlement 나오게 해보세요.
    print(item['date'] + "," +item['settlement'])
