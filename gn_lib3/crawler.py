import requests
from bs4 import BeautifulSoup

def getPrice(code):
    url = "https://finance.naver.com/item/main.nhn?code="+code
    print(url)
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    p_no_today = bs_obj.find("p", {"class":"no_today"})
    span_blind = p_no_today.find("span", {"class":"blind"})

    company_name_div = bs_obj.find("div", {"class":"wrap_company"})
    company_name = company_name_div.find("a").text
    # 전일가
    table_no_info = bs_obj.find("table", {"class":"no_info"})
    td_first = table_no_info.find("td", {"class":"first"})
    yesterday_span_blind = td_first.find("span", {"class":"blind"})

    # 고가, 저가
    high_em_no_up = table_no_info.find("em", {"class":"no_up"})
    high_blind = high_em_no_up.find("span", {"class":"blind"})


    return {
            "company_name":company_name,
            "now":span_blind.text,
            "yesterday":yesterday_span_blind.text,
            "high":high_blind.text
            }
