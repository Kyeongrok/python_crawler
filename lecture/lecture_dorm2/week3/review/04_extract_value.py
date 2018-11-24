from urllib. request import urlopen
from bs4 import BeautifulSoup # tree 구조로 접근할 수 있게 해줌

def get_bs_obj(url):
    html = urlopen(url)
    bs_obj = BeautifulSoup(html.read(), "html.parser")
    return bs_obj

def get_price(bs_obj):
    today = bs_obj.find("div",{"class":"today"})
    blind = today.find("span",{"class":"blind"})
    today_price = blind.text
    return today_price

url = "https://finance.naver.com/item/main.nhn?code=215600"
bs_obj = get_bs_obj(url)
price = get_price(bs_obj)
print(price)
