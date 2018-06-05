import requests
from bs4 import BeautifulSoup

url = "https://bp.eosgo.io/"


result = requests.get(url =url)
bs_obj = BeautifulSoup(result.content, "html.parser")

lf_items = bs_obj.findAll("div", {"class":"lf-item"})


hrefs = [div.find("a")['href'] for div in lf_items ]



for href in hrefs:
    try:
        sub_result = requests.get(href)
        sub_bs_obj = BeautifulSoup(sub_result.content, "html.parser")
        cover_buttons = sub_bs_obj.find("div", {"class":"buttons medium button-outlined"})
        link = cover_buttons.find("a")['href']
        print(link)
    except:
        print("except")






