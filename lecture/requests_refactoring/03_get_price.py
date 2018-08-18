# crawling 하는 코드
import requests
from bs4 import BeautifulSoup

# url을 넣어서 bs_obj를 return하는 function
def get_bs_obj(url):
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

url = "https://finance.naver.com/item/main.nhn?code=005930"
bs_obj = get_bs_obj(url)
no_today = bs_obj.find("p", {"class":"no_today"})
blind = no_today.find("span", {"class":"blind"})

print(blind.text)
