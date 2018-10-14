from urllib.request import urlopen
from bs4 import BeautifulSoup  # tree 구조로 접근할 수 있게 해줌

def get_bs_obj(url):
    html = urlopen(url)
    bs_obj = BeautifulSoup(html.read(), "html.parser")
    return bs_obj

def get_price(bs_obj):
    today = bs_obj.find("div",{"class":"today"})
    blind = today.find("span",{"class":"blind"})
    today_price = blind.text

    # close 전일
    close_td = bs_obj.find("td", {"class":"first"})
    close_blind = close_td.find("span",{"class":"blind"})
    close_price = close_blind.text
    # dictionray 딕셔너리
    return {"today":today_price, "close":close_price}



# 신라젠 215600, sk하이닉스 000660 셀트리온 068270
# 오뚜기 007310, 삼성전자 005930

url = "https://finance.naver.com/item/main.nhn?code=215600"
price = get_price(get_bs_obj(url))
print(price)

