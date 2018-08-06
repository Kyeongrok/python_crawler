import requests
from bs4 import BeautifulSoup

def get_bs_obj(url):
    html = requests.get(url)

    print(html.content)
    return BeautifulSoup(html.content, "html.parser")

url = "https://www.gopax.co.kr/"
bs_obj = get_bs_obj(url)

print(bs_obj)