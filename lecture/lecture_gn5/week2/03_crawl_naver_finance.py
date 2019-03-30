import requests

def crawl():
    url = "https://finance.naver.com/item/main.nhn?code=017800"
    response = requests.get(url)
    print(response)
    return response.content

pageString = crawl()
print(pageString)