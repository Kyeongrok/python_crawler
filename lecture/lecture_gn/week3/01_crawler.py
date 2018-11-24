import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=068270"
result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")
p_no_today = bs_obj.find("p", {"class":"no_today"}) # 서울시 강남구 역삼동
span_blind = p_no_today.find("span", {"class":"blind"})

print(span_blind.text)   # <span class="blind">228,000</span>