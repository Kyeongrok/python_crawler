# 실습2 해외곡물시장정보 사이트에서 알아낸 url을 호출해서 데이터를 console에 출력해보세요
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json


url = "http://grains.krei.re.kr/chart/main_chart/index/kind/S/sdate/2008-01-01/edate/2018-03-31"
html = urlopen(url)
bsObj = BeautifulSoup(html, "html.parser")

# json string을 json object로
jsonObject = json.loads(str(bsObj))

zero_to_nine = jsonObject

print(zero_to_nine)

# 실습3 zero_to_nine출력 해보기
for element in zero_to_nine:
    print(element)
    row = "{},{},{},{}".format(element['id'],element['date'],element['settlement'],element['volume'])
    print(row)

# [] list, array
# {} element요소, attribute속성, item아이템
# :앞에 있는것 property속성
# 속성 구분은 ,로 한다.
# 마지막 요소 뒤에는 ,를 빼준다.

'''
[
    {"이름":"cozy 모임공간", "가격":2500, "위치":"강남역 3번출구"},
    {"이름":"스터디 플래닛", "가격":3000, "위치":"역삼동"},
    {"이름":"에이지스토리", "가격":2000, "위치":"서울대입구"}
]
'''
