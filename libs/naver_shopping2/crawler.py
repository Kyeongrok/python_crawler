import requests

def crawl(keyword):
    url = f'https://search.shopping.naver.com/search/all?query={keyword}&cat_id=&frm=NVSHATC'
    data = requests.get(url)
    print(data.status_code, url)
    return data.content