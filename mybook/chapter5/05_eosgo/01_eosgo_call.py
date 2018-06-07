import requests
from bs4 import BeautifulSoup

url = "https://bp.eosgo.io/"

result = requests.get(url =url)

bs_obj = BeautifulSoup(result.content, "html.parser")
print(bs_obj)

