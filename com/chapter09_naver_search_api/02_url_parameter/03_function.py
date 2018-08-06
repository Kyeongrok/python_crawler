import requests
from urllib.parse import urlparse

def get_api_result(keyword, display):
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword + "&display=" + str(display)
    result = requests.get(urlparse(url).geturl(),
          headers={"X-Naver-Client-Id":"H1DC13DICQ8zIK84XwWn",
                   "X-Naver-Client-Secret":"8sUQqFukKQ"})
    return result.json()

keyword = "강남역"
json_obj = get_api_result(keyword, 100)

print(json_obj['display'])
print(json_obj['start'])
print(len(json_obj['items']))