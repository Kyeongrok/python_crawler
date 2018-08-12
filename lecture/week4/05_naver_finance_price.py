# 네이버 금융에서 035420코드 '네이버'의
# 현재가(771,000) 가지고 오기
#
# 1.get_bs_obj(url) function 만들어서 할 것
#
# 검색
# python에서 http호출 하는 법
# bs4에서 find사용하는 법
#
# 2.종목코드 바꾸면 결과가 다르게 나오도록
# function을 리팩토링 해볼것
# ex) get_price(company_code):
#
# 자판 바꾸기 ctrl + spac

import urllib.request

import bs4

def get_bs_obj(url):
    html = urllib.request.urlopen(url)
    bs_obj =bs4.BeautifulSoup(html, "html.parser")
    return bs_obj

def get_price(company_code):
    url="https://finance.naver.com/item/main.nhn?code=" + company_code
    bs_obj=get_bs_obj(url)
    today_stock = bs_obj.find("p", {"class" : "no_today"})
    blind=today_stock.find("span", {"class" : "blind"})
    return blind.text

print(get_price("005680"))