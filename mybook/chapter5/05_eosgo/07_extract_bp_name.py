import requests
from bs4 import BeautifulSoup

url = "https://bp.eosgo.io/listing/eos-canada/"

result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")

profile_name = bs_obj.find("div", {"class":"profile-name"})

print(profile_name)