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

def call_and_print(keyword, page):
    json_obj = get_api_result(keyword, 100, page)
    for item in json_obj['items']:
        print(item)

keyword = "강남역"
call_and_print(keyword, 1)
call_and_print(keyword, 101)
call_and_print(keyword, 201)
call_and_print(keyword, 301)
call_and_print(keyword, 401)
