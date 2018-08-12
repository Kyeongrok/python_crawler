import requests
from bs4 import BeautifulSoup

def get_bs_obj():
    url = "https://finance.naver.com/item/main.nhn?code=035420"
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

bs_obj = get_bs_obj()
today = bs_obj.find("div",{"class":"today"})


