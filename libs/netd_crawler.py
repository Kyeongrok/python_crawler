import requests
from bs4 import BeautifulSoup
# ctrl + tab
# window: ctrl + e, mac: command + e

def getLinks(start):
    url = "http://www.netd.ac.za/portal/?action=browse&category=Affiliation&maxresults=100&start=" + str(start) +"&order=asc"
    result = requests.get(url)
    print(start, result)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    ol = bs_obj.find("ol")
    lis = ol.findAll("li")
    links = []
    for li in lis:
        link = "http://www.netd.ac.za/" + li.find("a")["href"]
        links.append(link)

    return links
