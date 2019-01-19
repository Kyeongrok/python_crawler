import requests
# naver finance에서 page호출하기
def crawl(code):
    url = "https://finance.naver.com/item/main.nhn?code={}".format(code)
    data = requests.get(url)
    return data.content
