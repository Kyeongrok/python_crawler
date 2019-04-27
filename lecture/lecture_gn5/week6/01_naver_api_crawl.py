import requests
# 네이버 API에서 검색결과를 1000개 수집하고 저장 해보세요.
import urllib.request

def crawl(keyword, start):
    encText = urllib.parse.quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?query={}&display=100&start={}".format(encText, start)
    data = requests.get(url, headers={
        "X-Naver-Client-Id":"K436yv9jW1WlsRicx8vc",
        "X-Naver-Client-Secret":"GRivIwyqaB"
    })
    print(data, url)
    return data.json()

kewordResult = []
for page in range(1, 10 + 1):
    jsonObj = crawl("강남역 맛집", page * 100 - 99)
    items = jsonObj['items']
    kewordResult = kewordResult + items
print(len(kewordResult))

import json
file = open("./gangnam.json", "w+")
file.write(json.dumps(kewordResult))
