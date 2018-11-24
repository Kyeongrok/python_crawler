import requests
from urllib.parse import urlparse

def search_result(keyword):
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword
    result = requests.get(urlparse(url).geturl(),
          headers={"X-Naver-Client-Id":"JyP8ZGwBvgwzajxGWs7m",
                   "X-Naver-Client-Secret":"WC3_t8TCMu"})
    return(result.json())

result = search_result("남도학숙")

print(result['lastBuildDate'])
print(result['total'])
print(result['start'])
print(result['display'])
print(result['items'])


