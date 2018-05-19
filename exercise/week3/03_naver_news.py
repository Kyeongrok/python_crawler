import urllib.request
import bs4

url = "http://news.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

ul = bs_obj.find("ul", {"class":"newsnow_txarea"})
strongs = ul.findAll("strong")

for strong in strongs:
    print(strong.text)



