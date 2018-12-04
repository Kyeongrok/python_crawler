import requests
from bs4 import BeautifulSoup

url = "http://www.netd.ac.za/portal/?action=browse&category=Affiliation&maxresults=10&start=1&order=asc"
result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")
# http://www.netd.ac.za/?action=view&identifier=oai%3Aunion.ndltd.org%3Acput%2Foai%3Alocalhost%3A20.500.11838%2F727

ol = bs_obj.find("ol")
lis = ol.findAll("li")
for li in lis:
    print("http://www.netd.ac.za/" + li.find("a")["href"])

