import requests

def get_text(url):
    middle = requests.get(url)
    return middle.content


url = "https://finance.naver.com/marketindex/exchangeDetail.nhn?marketindexCd=FX_USDKRW"
result = get_text(url)
print(result)
