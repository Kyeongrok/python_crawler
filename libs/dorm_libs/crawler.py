import requests
from bs4 import BeautifulSoup

def getPrice(code):
    url = "https://finance.naver.com/item/main.nhn?code="+code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")

    no_today = bs_obj.find("p", {"class":"no_today"})
    blind = no_today.find("span", {"class":"blind"})

    table_no_info = bs_obj.find("table", {"class":"no_info"})
    td_first = table_no_info.find("td", {"class":"first"})
    yesterday_blind = td_first.find("span", {"class":"blind"})
    return {"close":blind.text, "yesterday":yesterday_blind.text}

print(getPrice("006840"))