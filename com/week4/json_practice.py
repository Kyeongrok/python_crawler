import json

json_string = '[{"이름":"cozy 모임공간", "가격":2500, "위치":"강남역 3번출구"},{"이름":"스터디 플래닛", "가격":3000, "위치":"역삼동"},{"이름":"에이지스토리", "가격":2000, "위치":"서울대입구"}]'
json_object = json.loads(json_string)
# [{}, {}, {}]

print(json_object)

# 하나씩 꺼내서 출력 해보세요 for문
for item in json_object:
    result = "{},{},{}".format(item['이름'],item['가격'],item['위치'])
    print(result)
