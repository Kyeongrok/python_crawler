import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/item/board.nhn?code=096240'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) 26.109 Safari/537.36"
}
req = requests.get(url, headers)

contents = req.content
soup = BeautifulSoup(contents,'html.parser')
print(soup)