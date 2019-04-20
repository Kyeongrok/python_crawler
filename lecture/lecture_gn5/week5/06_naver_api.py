import urllib.request
import requests

def crawl():
    encText = urllib.parse.quote("강남역 평양냉면")
    url = "https://openapi.naver.com/v1/search/blog?query={}&display=100&start={}".format(encText, 2) # json 결과
    data = requests.get(url, headers={
        "X-Naver-Client-Id":"K436yv9jW1WlsRicx8vc",
        "X-Naver-Client-Secret":"GRivIwyqaB"
    })
    return data.json()

resultJson = crawl()
print(resultJson['total'])
print(resultJson['start'])
print(resultJson['display'])
items = resultJson['items']

for item in items:
    print(item)

import json
file = open("./nangmyn.json", "w+")
file.write(json.dumps(items))


