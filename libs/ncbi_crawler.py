import requests
from bs4 import BeautifulSoup

def getNetdLinks(start):
    url = "https://www.ncbi.nlm.nih.gov/pubmed"
    result = requests.post(url, data={
        "term": "(\"Acute Myeloid Leukemia\") OR \"AML\"",
        "coll_start": str(start),
        "EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.PageSize": "200"
    })
    print(start, result.status_code)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    rprts = bs_obj.findAll("div", {"class":"rprt"})
    links = []
    for item in rprts:
        atag = item.find("a")
        link = "https://www.ncbi.nlm.nih.gov" + atag["href"]
        links.append(link)
    return links

def getSubPageContent(pageString):
    bs_obj = BeautifulSoup(pageString, "html.parser")
    cit = bs_obj.find("div", {"class":"cit"})
    journal = cit.text.split(" doi")[0]
    rprt_all = bs_obj.find("div", {"class":"rprt_all"})
    title = rprt_all.find("h1").text
    afflist = bs_obj.find("div", {"class":"afflist"})
    dds = afflist.findAll("dd")
    authors = [dd.text for dd in dds]
    abstr = bs_obj.find("div", {"class":"abstr"})
    abstract = abstr.find("div").text
    keywords = bs_obj.find("div", {"class":"keywords"}).text
    keywords = keywords.split("; ")
    return {"journal": journal, "title":title, "authors":authors, "abstract":abstract, "keywords":keywords}