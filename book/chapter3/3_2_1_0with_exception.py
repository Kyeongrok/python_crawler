from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse
import datetime
import re
import random
random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("https://ko.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html.read(), "html.parser")

    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p").get_text())
        print(bsObj.find(id="mw-content-text").findAll("p").get_text())
    except AttributeError:
        print("This page is missing something!")

    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/%EC%8B%A0%EC%82%AC%EB%8F%99_(%EA%B0%95%EB%82%A8%EA%B5%AC)")