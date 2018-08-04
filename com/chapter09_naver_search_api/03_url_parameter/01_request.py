import requests
from urllib.parse import urlparse

keyword = "강남역"
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword
result = requests.get(urlparse(url).geturl(),
          headers={"X-Naver-Client-Id":"H1DC13DICQ8zIK84XwWn",
                   "X-Naver-Client-Secret":"8sUQqFukKQ"})

json_obj = result.json()
print(json_obj['display'])
print(json_obj['start'])
print(len(json_obj['items']))