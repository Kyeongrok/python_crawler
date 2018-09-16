from urllib.parse import urlparse

import requests


def search_result(keyword):
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword + "&display=100"
    print(url)
    result = requests.get(urlparse(url).geturl(),
          headers={"X-Naver-Client-Id":"JyP8ZGwBvgwzajxGWs7m",
                   "X-Naver-Client-Secret":"WC3_t8TCMu"})
    return(result.json())

result = search_result("남도학숙")

for item in result['items']:
    title = item['title'].replace('<b>', "").replace('</b>',"")
    print(title + '@'+item['bloggername']+'@'+item['bloggerlink']+'@'+item['postdate'])

