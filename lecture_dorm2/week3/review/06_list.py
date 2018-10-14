from urllib.request import urlopen
from bs4 import BeautifulSoup  # tree 구조로 접근할 수 있게 해줌

def get_bs_obj(url):
    html = urlopen(url)
    bs_obj = BeautifulSoup(html.read(), "html.parser")
    return bs_obj

def get_price(bs_obj):
    no_today = bs_obj.find("div",{"class":"today"})
    blind = no_today.find("span",{"class":"blind"})
    today_price = blind.text

    # close 전일
    close_td = bs_obj.find("td", {"class":"first"})
    close_blind = close_td.find("span",{"class":"blind"})
    close_price = close_blind.text
    # dictionray 딕셔너리
    table = bs_obj.find("table", {"class":"no_info"})
    trs = table.findAll("tr")
    print(trs[1]) # [<tr></tr>, <tr></tr>]

    return {"today":today_price, "close":close_price}



# 신라젠 215600, sk하이닉스 000660 셀트리온 068270
# 오뚜기 007310, 삼성전자 005930
code_list = ["215600", "000660"]
for code in code_list:
    url = "https://finance.naver.com/item/main.nhn?code=" + code
    price = get_price(get_bs_obj(url))
    print(price)
