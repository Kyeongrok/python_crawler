import requests
from bs4 import BeautifulSoup

def get_bs_obj(url):
    middle = requests.get(url)
    bs_obj = BeautifulSoup(middle.content, "html.parser")
    return bs_obj


# url = "https://finance.naver.com/marketindex/exchangeDetail.nhn?marketindexCd=FX_USDKRW"
url = "https://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_USDKRW"
bs_obj = get_bs_obj(url)
print(bs_obj)
