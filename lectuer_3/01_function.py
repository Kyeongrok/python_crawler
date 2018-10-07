# 라이브러리
import requests

def get_page(url):
    result = requests.get(url)
    print(result.content)

url = "https://finance.naver.com/marketindex/worldDailyQuote.nhn?marketindexCd=OIL_CL&fdtc=2"
get_page(url)