import requests
import bs4

url = "http://jolse.com/category/face/42/"
result = requests.get(url)

bs_obj = bs4.BeautifulSoup(result.content, "html.parser")

ul = bs_obj.find("ul", {"class":"prdList column5"})

ps = ul.findAll("p", {"class":"name"})

links = ["http://jolse.com"+item.find("a")['href'] for item in ps]

def getInfos(url):
    result = requests.get(url)
    bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
    print(bs_obj)
    desc = bs_obj.find("div", {"id":"jolseProduct"})
    print(desc)

for item in links:
    getInfos(item)

