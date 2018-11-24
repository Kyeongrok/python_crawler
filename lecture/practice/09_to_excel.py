import requests
from urllib.parse import urlparse

def get_json_obj(keyword, start_at):
    url = "https://openapi.naver.com/v1/search/blog.json?query=" + \
          keyword + "&display=100" + "&start=" + str(start_at)
    result = requests.get(urlparse(url).geturl(),
              headers={"X-Naver-Client-Id":"PqQ1Z3ohPXR5U6B_Ol2W",
                       "X-Naver-Client-Secret":"rSaY31bKRi"})

    return result.json()

result = get_json_obj("역삼 운동", 1)
list = result["items"]

file = open("./hello.csv", "w+",encoding="utf-8")
for item in list:
    # print(item["bloggername"] + "@" + item['title'])
    file.write(item["link"] + "\n")
