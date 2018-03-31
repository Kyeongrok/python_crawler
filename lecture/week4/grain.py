# 실습2 해외곡물시장정보 사이트에서 알아낸 url을 호출해서 데이터를 console에 출력해보세요
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json


url = "http://grains.krei.re.kr/chart/main_chart/index/kind/S/sdate/2008-01-01/edate/2018-03-31"
html = urlopen(url)
bsObj = BeautifulSoup(html, "html.parser")

# json string을 json object로
jsonObject = json.loads(str(bsObj))


zero_to_nine = jsonObject[0:10]

print(zero_to_nine)

# 실습3 zero_to_nine출력 해보기

for element in zero_to_nine:
    row = "{},{},{},{}".format(element['id'],element['date'],element['settlement'],element['volume'])
    print(row)


