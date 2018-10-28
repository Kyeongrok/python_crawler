import requests
from bs4 import BeautifulSoup

def getPrice(code):
    url = "https://finance.naver.com/item/main.nhn?code="+code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    p_no_today = bs_obj.find("p", {"class":"no_today"})
    span_blind = p_no_today.find("span", {"class":"blind"})

    return span_blind.text   # <span class="blind">228,000</span>
