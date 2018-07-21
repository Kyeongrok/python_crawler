import requests
from urllib.parse import urlparse

url = "https://openapi.naver.com/v1/search/blog?query=보험"
result = requests.get(urlparse(url).geturl(),
                      headers={"X-Naver-Client-Id":"H1DC13DICQ8zIK84XwWn",
                               "X-Naver-Client-Secret":"8sUQqFukKQ"})
json = result.json()
print(json['lastBuildDate'])
print(json['total'])
print(json['start'])
print(json['items'])

titles = [ item['title'] for item in json['items']]
for title in titles:
    print(title)