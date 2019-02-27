import requests
import bs4

url = "http://jolse.com/category/tonermist/43/"

# 403 Forbidden 에러가 발생 할 경우 아래 Headers를 추가 해 줍니다.
# http://www.useragentstring.com/ 에 접속하여 "User-Agent" 에 추가 해줍니다.
headers = {
    "User-Agent": "*** 이곳에 해당하는 User-Agent를 추가합니다 (예시), Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) 26.109 Safari/537.36*******"
}
result = requests.get(url, headers=headers)
bs_obj = bs4.BeautifulSoup(result.content, "html.parser")

print(bs_obj)
