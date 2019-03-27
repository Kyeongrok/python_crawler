import requests
from bs4 import BeautifulSoup

def crawl():
    url = "http://www.holybible.or.kr/BIBLE_hkjv/"
    data = requests.get(url)
    print(data)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")



