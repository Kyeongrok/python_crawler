import urllib.request
import bs4

url = "http://www.nate.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")
divignb = bs_obj.find("div", {"id":"divignb"})
print(divignb)
print(divignb.find("li").text)