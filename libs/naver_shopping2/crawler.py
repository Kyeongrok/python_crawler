import requests

def crawl(keyword):
    url = "https://search.shopping.naver.com/search/all.nhn?query=숨셔바요&cat_id=&frm=NVSHATC"
    data = requests.get(url)
    print(data.status_code, url)
    return data.content