from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_bs_obj(url):
    # html받아오기
    html = urlopen(url) # 크롤링을 해서
    # print(html.read())
    # 영어 번역가, 아랍어 아랍어 번역가 html, xml,
    bs_obj = BeautifulSoup(html.read().decode("euc-kr"), "html.parser")    # 파싱
    return bs_obj

def get_price(bs_obj):
    no_today = bs_obj.find("p", {"class":"no_today"})
    blind = no_today.find("span", {"class":"blind"})
    # print(blind)
    return blind.text

url = "https://finance.naver.com/item/main.nhn?code=000660"
bs_obj = get_bs_obj(url)
price = get_price(bs_obj)
print(price)