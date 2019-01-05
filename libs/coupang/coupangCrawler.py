import requests

def getString(url):
    data = requests.get(url)
    return data.content