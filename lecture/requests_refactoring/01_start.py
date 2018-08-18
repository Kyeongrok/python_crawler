# crawling 하는 코드
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=005930"
result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")
print(bs_obj)
