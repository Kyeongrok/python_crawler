# 라이브러리
import requests
from bs4 import BeautifulSoup

def get_page(url):
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    tbl_exchange = bs_obj.find("table", {"class":"tbl_exchange"})
    tbody = tbl_exchange.find("tbody")
    trs = tbody.findAll("tr")

    for tr in trs:
        tds = tr.findAll("td")
        print(tds[0].text.strip()+"@"+tds[1].text.strip())

    return bs_obj

url = "https://finance.naver.com/marketindex/worldDailyQuote.nhn?marketindexCd=OIL_CL&fdtc=2"
url = "https://finance.naver.com/marketindex/oilDetail.nhn?marketindexCd=OIL_GSL"
bs_obj = get_page(url)
# print(bs_obj)