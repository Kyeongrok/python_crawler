# 네이버 금융 페이지 불러오기
from libs.naver_finance.crawler import crawl
from libs.naver_finance.parser import parse

# sk하이닉스, 신한지주
print(parse(crawl("000660")))
print(parse(crawl("055550")))
