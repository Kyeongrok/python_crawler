import requests
from bs4 import BeautifulSoup

url = "https://bp.eosgo.io/"

result = requests.get(url =url)
bs_obj = BeautifulSoup(result.content, "html.parser")

lf_items = bs_obj.findAll("div", {"class":"lf-item"})

hrefs = [div.find("a")['href'] for div in lf_items ]

print(len(hrefs))

