import requests

def crawl(keyword):
    url = "https://search.shopping.naver.com/search/all.nhn?query={}&cat_id=&frm=NVSHATC".format(keyword)
    data = requests.get(url)
    print(data)
    return data.content