# 라이브러리 임포트하기
# page call => 크롤링 crawling
# data 뽑아내기 => 파싱 parsing

import urllib.request # 전화 걸기 page call
import bs4 # 파싱하는 라이브러리

# bs4 BeautifulSoup4 뷰티풀솝 -> 파싱

url = "https://finance.naver.com/item/main.nhn?code=068270"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html.read().decode("euc-kr"), "html.parser")

# 서울시 -> 강남구 -> 역삼로7길 -> 17 -> 네스빌 -> 510
# 1장 -> 1절 -> a ->
# 마태복음 -> 1장 -> 10절
# 논어 -> 학이편 -> 12 -> 2절
# 트리구조
print(bs_obj)