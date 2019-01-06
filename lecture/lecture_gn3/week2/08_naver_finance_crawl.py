# hello를 return하는 crawl이라는 이름의 함수를 만들어보세요
import requests

# url -> string = 크롤링 -> 크롤러 crawler
# string -> [], {} 파싱 -> 파서 parser

def crawl():
    url = "https://finance.naver.com/item/main.nhn?code=068270"
    data = requests.get(url)
    return data.content

print(crawl())