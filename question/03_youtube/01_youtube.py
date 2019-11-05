
import requests
from bs4 import BeautifulSoup

def crawl(url):
    res = requests.get(url)
    # print(res)
    return res.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    lockupContents = bsObj.findAll("div", {"class":"yt-lockup-content"})
    lockupContent = lockupContents[0]

    print(lockupContent)
    # contents = bsObj.find("div", {"id":"contents"})
    #https: // www.youtube.com / watch?v = xi9OgtDoa4M
    # print(bsObj)


url = "https://www.youtube.com/results?search_query=발레"
pageString = crawl(url)
list = parse(pageString)
# print(pageString)