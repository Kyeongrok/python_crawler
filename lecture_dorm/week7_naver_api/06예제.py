import requests
from urllib.parse import urlparse

def search_result(keyword):
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword

    result = requests.get(urlparse(url).geturl(),
          headers={"X-Naver-Client-Id":"JyP8ZGwBvgwzajxGWs7m",
                   "X-Naver-Client-Secret":"WC3_t8TCMu"})
    return(result.json())

result = search_result("남도학숙")

print(result['items'][0]['title'])
print(result['items'][1]['title'])
print(result['items'][2]['title'])
print(result['items'][3]['title'])
print(result['items'][4]['title'])
print(result['items'][5]['title'])
print(result['items'][6]['title'])
print(result['items'][7]['title'])
print(result['items'][8]['title'])
print(result['items'][9]['title'])