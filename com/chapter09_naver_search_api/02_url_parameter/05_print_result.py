import requests
from urllib.parse import urlparse

def get_api_result(keyword, display, start):
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword \
          + "&display=" + str(display) \
          + "&start=" + str(start)
    result = requests.get(urlparse(url).geturl(),
          headers={"X-Naver-Client-Id":"H1DC13DICQ8zIK84XwWn",
                   "X-Naver-Client-Secret":"8sUQqFukKQ"})
    return result.json()

keyword = "강남역"
json_obj = get_api_result(keyword, 100, 1)

for item in json_obj['items']:
    print(item)