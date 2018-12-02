import requests
import urllib.parse

def get1000Result(keyword):
    list = []
    for num in range(0, 10):
        list = list + call(keyword, num * 100 + 1)['items']
    return list

def call(keyword, startNum):
    encText = urllib.parse.quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?query=" \
          + encText + "&display=100" + "&start=" + str(startNum)
    result = requests.get(url, headers={
        "X-Naver-Client-Id":"JyP8ZGwBvgwzajxGWs7m",
        "X-Naver-Client-Secret":"WC3_t8TCMu"
    })
    print(keyword, result)
    return result.json()
