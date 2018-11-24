import requests
from bs4 import BeautifulSoup

# naver = 035420 113,000 068270
def getPrice(code):
    url = "https://finance.naver.com/item/main.nhn?code="+code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    p_no_today = bs_obj.find("p", {"class":"no_today"})
    span_blind = p_no_today.find("span", {"class":"blind"})
    print(span_blind.text)   # <span class="blind">228,000</span>

codes = [
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
    "190150",
    "195970",
]

for code in codes:
    try:
        getPrice(code)
    except:
        print("error:", code)