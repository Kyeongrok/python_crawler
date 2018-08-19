import urllib.request

import bs4


def get_bs_obj(url):
    html = urllib.request.urlopen(url)
    bs_obj =bs4.BeautifulSoup(html, "html.parser")
    return bs_obj

def get_price(company_code):
    url = "https://finance.naver.com/item/main.nhn?code="
    url = url + company_code
    bs_obj = get_bs_obj(url)
    today_stock = bs_obj.find("p",{"class":"no_today"})
    blind = today_stock.find("span",{"class":"blind"})
    td_first = bs_obj.find("td", {"class":"first"})

    # 종가
    blind_close = td_first.find("span", {"class":"blind"})
    close = blind_close.text

    # 고가
    high_price = bs_obj.find('em', {'class': 'no_up'})
    blind_high = high_price.find('span', {'class':'blind'})

    #시가
    no_down = bs_obj.findAll("em", {"class":"no_down"})
    open = no_down[3].find("span", {"class":"blind"}).text

    return {"now_price":blind.text, "close":close,
            'high_price':blind_high.text, "open":open}

print(get_price("005930"))