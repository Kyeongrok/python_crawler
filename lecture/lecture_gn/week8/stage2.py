from gn_lib3.naver_api_caller2 import get1000Result
import json
# 1000개씩 두번 나오는 list를 하나의 list로 합치기
# 합친 list를 json으로 저장하기

list = []
keywords = ["강남역 영화", "강남역 맛집", "강남역 저녁",
            "강남역 데이트", "강남역 맞선", "강남역 여친",
            "강남역 강의", "강남역 파이썬", "강남역 python",
            "강남역 엑셀"
            ]
for keyword in keywords:
    result = get1000Result(keyword)
    list = list + result

file = open("./search_result.json", "w+")
file.write(json.dumps(list))
