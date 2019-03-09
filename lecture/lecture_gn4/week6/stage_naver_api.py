import requests
import urllib.request
import json

def crawl(keyword, startNo):
    encText = urllib.parse.quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?display=100&query={}&start={}".format(encText, startNo)  # json 결과
    headers = {
        "X-Naver-Client-Id":"ag4BDzghpk894x9cD0Vb",
        "X-Naver-Client-Secret":"IfDaFAoqKn"
    }
    data = requests.get(url, headers=headers)
    print(data)
    return data.json()

result = []
for no in range(0, 10):
    jsonResult = crawl("캡틴 마블", no * 100 + 1) # 1, 2, 3, 4 | 1, 101, 201, 301
    items = jsonResult['items']
    result = result + items

file = open("./captin_marble.json", "w+")
file.write(json.dumps(result))


