from urllib.parse import urlparse

url = "http://www.naver.com?query=검색어"

print(urlparse(url).geturl())
