from urllib.request import urlopen
import json

from_date = "2018-01-01"
to_date = "2018-01-31"
url = "http://grains.krei.re.kr/chart/main_chart/index/kind/W/sdate/" + from_date + "/edate/" + to_date
text = urlopen(url)

json_obj = json.load(text)

datas = [item['settlement'] for item in json_obj]

print(datas)


