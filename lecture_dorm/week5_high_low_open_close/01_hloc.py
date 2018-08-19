import requests
from bs4 import BeautifulSoup

def get_bs_obj():
    url = "https://finance.naver.com/item/main.nhn?code=005930"
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

# table을 넣으면 시고저종이 나오는 function
bs_obj = get_bs_obj()
no_info = bs_obj.find("table", {"class":"no_info"})
tr = no_info.find("tr")
print(tr)
td_first = tr.find("td")
print(td_first.find("span", {"class":"blind"}).text)

# {} json에 대해
# list에 대해
# findAll()에 대해
