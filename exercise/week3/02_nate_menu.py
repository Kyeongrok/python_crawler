import urllib.request
import bs4

url = "http://www.nate.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")
divGnb = bs_obj.find("div", {"id":"divGnb", "class":"area_gnb"})

lis = divGnb.find("ul").findAll("li")

for li in lis[0:11]:
    print(li.find("a").text)

