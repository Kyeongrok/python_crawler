import requests
from bs4 import BeautifulSoup

def get_bs_obj(url):
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

url = "https://news.naver.com/"
result = get_bs_obj(url)
print(result)