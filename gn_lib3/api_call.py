import requests
from urllib.parse import urlparse
# keyword를 받아서 검색 결과를 return해줌

def naverApiCall(keyword):
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword # json 결과
    result = requests.get(urlparse(url).geturl(),
                  headers={"X-Naver-Client-Id":"bmMn9JNtSywmpiVmsqkO",
                          "X-Naver-Client-Secret":"e2u6Dw4w0c"})
    return result.json()
