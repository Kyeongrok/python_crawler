from libs.naver_api.naver_api_caller import get1000result
file = open("./result.json", "w+", encoding="utf-8")

list = []
keywords = ["강남역 맛집", "강남역 공연", "강남역 python"]
for keyword in keywords:
    list = list + get1000result(keyword)

import json
file = open("./data.json", "w+")
file.write(json.dumps(list))
