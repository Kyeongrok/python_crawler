import requests
from bs4 import BeautifulSoup

url = "http://www.netd.ac.za/?action=browse&category=Affiliation&order=asc"
result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")

ol = bs_obj.find("ol")
lis = ol.findAll("li")
urlPrefix = "http://www.netd.ac.za/"
for li in lis:
    print(urlPrefix + li.find("a")["href"])
