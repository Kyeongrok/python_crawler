from libs.naver_api.naver_api_caller import get1000Result
import json

keywords = ["강남역 공연", "강남역 맛집", "강남역 오피스텔"]
list = []
for keyword in keywords:
    result = get1000Result("강남역 공연")
    list = list + result
print(len(list))
file = open("./search_result.json", "w+")
file.write(json.dumps(list))

