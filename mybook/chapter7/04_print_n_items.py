from urllib.request import urlopen
import json

url = "http://grains.krei.re.kr/chart/main_chart/index/kind/W/sdate/1972-01-01/edate/2018-04-28"
html = urlopen(url)
jsonObjs = json.load(html)

print(jsonObjs[0])
