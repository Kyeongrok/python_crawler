import urllib.request
import bs4

def getPrice():
    url = "https://finance.naver.com/item/main.nhn?code=068270"
    html = urllib.request.urlopen(url)

    bs_obj = bs4.BeautifulSoup(html.read().decode("euc-kr"), "html.parser")
    # <p class="no_today">___</p> # 서울시 강남구
    no_today = bs_obj.find("p", {"class":"no_today"})
    blind = no_today.find("span", {"class":"blind"})
    #
    print(blind.text)

getPrice("068270")
getPrice("000660")
