import requests

def crawl(url):
    session = requests.Session()
    print(session.cookies)
    result = requests.get(url)
    print(result.status_code, url)
    return result.content