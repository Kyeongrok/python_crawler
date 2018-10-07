from urllib. request import urlopen
from bs4 import BeautifulSoup # tree 구조로 접근할 수 있게 해줌

def get_bs_obj(url):
    html = urlopen(url)
    bs_obj = BeautifulSoup(html.read().decode("euc-kr"),
                           "html.parser")
    return bs_obj

def get_price(bs_obj):
    today = bs_obj.find("div",{"class":"today"})
    return today

url = "https://finance.naver.com/item/main.nhn?code=215600"
price = get_price(get_bs_obj(url))
print(price)
#bs_obj = get_bs_obj(url)
#print(bs_obj)

