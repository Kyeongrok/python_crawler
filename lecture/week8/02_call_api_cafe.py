import requests
from urllib.parse import urlparse

def get_json_obj(keyword, start_at):
    url = "https://openapi.naver.com/v1/search/cafearticle.json?query=" + \
          keyword + "&display=100" + "&start=" + str(start_at)
    result = requests.get(urlparse(url).geturl(),
              headers={"X-Naver-Client-Id":"JyP8ZGwBvgwzajxGWs7m",
                       "X-Naver-Client-Secret":"WC3_t8TCMu"})

    return result.json()

for start_at in range(1, 1000, 100):
    json_obj = get_json_obj(keyword="파이썬", start_at=start_at)
    items = json_obj['items']
    for item in items:
        title = item['title'].replace("<b>","").replace("</b>","")
        cafename = item['cafename']
        result = "{}@{}".format(title, cafename)
        print(result)
