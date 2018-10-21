# 라이브러리 임포트하기
import urllib.request

url = "https://finance.naver.com/item/main.nhn?code=068270"
html = urllib.request.urlopen(url)

print(html.read())