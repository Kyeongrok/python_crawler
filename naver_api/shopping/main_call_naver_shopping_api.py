import requests
from urllib.parse import urlparse

def call_naver_shopping_api(keyword, display, start):
    url = "https://openapi.naver.com/v1/search/shop.json?query=" + keyword + "&display=" + str(display) + "&start=" + str(start)
    result = requests.get(urlparse(url).geturl(),
              headers={"X-Naver-Client-Id":"PqQ1Z3ohPXR5U6B_Ol2W",
                       "X-Naver-Client-Secret":"rSaY31bKRi"})
    return result.json()

print(call_naver_shopping_api('형광등', 100, 1))

