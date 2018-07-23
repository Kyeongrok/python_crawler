import requests
from bs4 import BeautifulSoup

url = "https://bp.eosgo.io/listing/eos-canada/"

result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")
print(bs_obj)
