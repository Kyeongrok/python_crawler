import requests
from bs4 import BeautifulSoup

def getPrice(code):
    url = "https://finance.naver.com/item/main.nhn?code="+code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")

    no_today = bs_obj.find("p", {"class":"no_today"})
    blind = no_today.find("span", {"class":"blind"})
    return blind.text


print("셀트리온", getPrice("068270"))
print("신라젠", getPrice("215600"))

list = [
    "060310",
    "095570",
    "068400",
    "006840",
    "054620",
    "265520",
    "211270",
    "152100",
    "222170",
    "161490",
    "161500",
    "161510",
    "189400",
    "190160",
    "213630",
    "190150"
        ]
