import requests
from urllib.parse import urlparse

keyword = "강남역"
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword
result = requests.get(urlparse(url).geturl(),
          headers={"X-Naver-Client-Id":"H1DC13DICQ8zIK84XwWn",
                   "X-Naver-Client-Secret":"8sUQqFukKQ"})

json_obj = result.json()
for item in json_obj['items']:
    print(item['title'].replace("<b>","").replace("</b>", ""))