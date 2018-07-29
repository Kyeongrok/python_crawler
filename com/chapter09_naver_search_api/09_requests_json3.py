import requests
from urllib.parse import urlparse

url = "https://openapi.naver.com/v1/search/blog?query=보험&start=11"
result = requests.get(urlparse(url).geturl(),
                      headers={"X-Naver-Client-Id":"H1DC13DICQ8zIK84XwWn",
                               "X-Naver-Client-Secret":"8sUQqFukKQ"})
json = result.json()
for item in json['items']:
    print(item['title'].replace("<b>","").replace("</b>", ""),
          item['link'])
