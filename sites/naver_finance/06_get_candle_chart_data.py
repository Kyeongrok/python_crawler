import requests
from bs4 import BeautifulSoup

def get_bs_obj(company_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

# bs_obj를 받아서 price를 return하게
def get_candle_chart_data(company_code):
    bs_obj = get_bs_obj(company_code)

    td_first = bs_obj.find("td", {"class":"first"})
    blind = td_first.find("span", {"class":"blind"})

    # close 종가(전일)
    close = blind.text

    return close

# sk하이닉스 000660
candle_chart_data = get_candle_chart_data("000660")
print(candle_chart_data)