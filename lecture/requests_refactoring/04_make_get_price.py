import requests
from bs4 import BeautifulSoup

# url을 넣어서 bs_obj를 return하는 function
def get_bs_obj(url):
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

# company_code를 받아서 price를 return하는 함수
def get_price(company_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    bs_obj = get_bs_obj(url)
    no_today = bs_obj.find("p", {"class":"no_today"})
    blind = no_today.find("span", {"class":"blind"})
    return blind.text

price_samsung = get_price("005930")
price_sk_hynix = get_price("000660")
print(price_samsung)
print(price_sk_hynix)
