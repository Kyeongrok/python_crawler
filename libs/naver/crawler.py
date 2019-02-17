import requests

def crawl(code):
    url = "https://finance.naver.com/item/main.nhn?code={}".format(code)
    data = requests.get(url)
    print(data.status_code)
    return data.content