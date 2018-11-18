import requests
from urllib.parse import urlparse
keyword = "강남역 맛집"
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword # json 결과
result = requests.get(urlparse(url).geturl(),
              headers={"X-Naver-Client-Id":"bmMn9JNtSywmpiVmsqkO",
                      "X-Naver-Client-Secret":"e2u6Dw4w0c"})
json_obj = result.json()
print(json_obj)
