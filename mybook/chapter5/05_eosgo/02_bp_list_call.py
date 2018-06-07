import requests
from bs4 import BeautifulSoup

url = "https://bp.eosgo.io/"


result = requests.get(url =url)

bs_obj = BeautifulSoup(result.content)
bp_names = bs_obj.findAll("h4", {"class":"case27-secondary-text listing-preview-title"})

lf_items = bs_obj.findAll("div", {"class":"lf-item"})

for bp_name in bp_names:
    print(bp_name.text)

print(len(bp_names))

