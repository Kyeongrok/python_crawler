import requests
from urllib.parse import quote

def getApiResult(keyword):
    # apiResult100을 10번 호출 하는 기능
    list = []
    # result['items']
    for num in range(0, 10):
        list += getApiResult100(keyword, 100*num + 1)['items']
        # 초항 1 등차 100 n = 0 to 9
        # 100 * num + 1
    return list

def getApiResult100(keyword, start):
    encText = quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?display=100&query={}&start={}".format(encText, start)

    data = requests.get(url, headers={
        "X-Naver-Client-Id":"l6_H64cWBZnHLGhZ7zKO",
        "X-Naver-Client-Secret":"dlNVIJaLeI"
    })
    print(data.status_code)
    return data.json()

