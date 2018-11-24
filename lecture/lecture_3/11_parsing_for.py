import requests
from bs4 import BeautifulSoup

def get_bs_obj(url):
    middle = requests.get(url)
    bs_obj = BeautifulSoup(middle.content, "html.parser")
    return bs_obj

def print_ratio(bs_obj):
    # 파싱 로직
    table = bs_obj.find("table", {"class":"tbl_exchange"})
    tbody = table.find("tbody")

    # [<tr></tr>, <tr></tr>, <tr></tr>]
    trs = tbody.findAll("tr")
    for tr in trs:
        date = tr.findAll("td")[0].text
        ratio = tr.findAll("td")[1].text
        before = tr.findAll("td")[2].text
        print(date, ratio, before)

# url = "https://finance.naver.com/marketindex/exchangeDetail.nhn?marketindexCd=FX_USDKRW"
url = "https://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_USDKRW"
bs_obj = get_bs_obj(url)
print_ratio(bs_obj)

