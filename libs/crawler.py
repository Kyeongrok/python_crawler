import requests

def crawl(url):
    result = requests.get(url)
    print(result.status_code)
    return result.content