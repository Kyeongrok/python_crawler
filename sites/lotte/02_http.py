import requests
from bs4 import BeautifulSoup
url = "https://display.ellotte.com/display-fo/categoryShop?dshopNo=10023"

result = requests.get(url)
bs_obj = BeautifulSoup(result.content)
print(bs_obj)