import requests
from bs4 import BeautifulSoup

url = "https://bp.eosgo.io/listing/eos-canada/"

result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")

profile_name = bs_obj.find("div", {"class":"profile-name"})

h1_bp_name = profile_name.find("h1")
bp_name = h1_bp_name.text

cover_buttons = bs_obj.find("div", {"class":"cover-buttons"})

button_label = bs_obj.find("span", {"class":"button-label"})
print(button_label)