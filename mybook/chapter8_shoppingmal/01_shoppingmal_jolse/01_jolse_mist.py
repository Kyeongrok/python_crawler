import requests
from bs4 import BeautifulSoup

url = "http://jolse.com/category/tonermist/43/"
result = requests.get(url)

bs_obj = BeautifulSoup(result.content, "html.parser")
print(bs_obj)