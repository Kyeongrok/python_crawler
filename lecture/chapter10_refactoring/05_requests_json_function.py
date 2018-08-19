from urllib.parse import urlparse
import requests

def get_json_obj(keyword, start):
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword + \
          "&display=100" + "&start=" + str(start)
    result = requests.get(urlparse(url).geturl(),
              headers={"X-Naver-Client-Id":"H1DC13DICQ8zIK84XwWn",
                       "X-Naver-Client-Secret":"8sUQqFukKQ"})
    return result.json()


for start_num in range(1, 600, 100):
    json_obj = get_json_obj("파이썬", start_num)
    for item in json_obj['items']:
        title = item['title'].replace("<b>", "").replace("</b>", "")
        link = item['link']
        bloggername = item['bloggername']
        print(title + "@" + link + "@" + bloggername)

