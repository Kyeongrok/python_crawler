import requests

def crawl():
    url = "https://search.shopping.naver.com/search/all.nhn?query=탈취제&cat_id=&frm=NVSHATC"
    data = requests.get(url)
    print(data)
    return data.content