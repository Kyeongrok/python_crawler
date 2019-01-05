import requests
from urllib.parse import quote

def crawl(keyword, start):
    # 검색했을때 검색결과
    encText = quote(keyword) # unicode encoding
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText \
          + "&display=100" + "&start={}".format(start)  # json 결과
    data = requests.get(url, headers={
        "X-Naver-Client-Id":"l6_H64cWBZnHLGhZ7zKO",
        "X-Naver-Client-Secret":"dlNVIJaLeI"
    })
    print(data.status_code, keyword)
    return data.json()