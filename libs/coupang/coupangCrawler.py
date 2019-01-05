import requests

def getString(url):
    data = requests.get(url)
    print(data.status_code, url)
    return data.content