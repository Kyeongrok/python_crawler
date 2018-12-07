import requests
from bs4 import BeautifulSoup
url = "https://www.ncbi.nlm.nih.gov/pubmed/?term=(%22Acute+Myeloid+Leukemia%22)+OR+%22AML%22"
result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")
content = bs_obj.find("div", {"class":"content"})
rprts = content.findAll("div", {"class":"rprt"})

for item in rprts:
    atag = item.find("a")
    link = "https://www.ncbi.nlm.nih.gov" + atag["href"]
    print(link, atag.text)

    linkResult = requests.get(link)
    subPage = BeautifulSoup(linkResult.content, "html.parser")
    print(subPage.find("div", {"class":"rprt_all"}))





