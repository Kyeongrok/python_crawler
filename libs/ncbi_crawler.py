import requests
from bs4 import BeautifulSoup
from seleniumrequests import Safari

def getSubPageContent(pageString):
    pageString = pageString.encode('utf-8')
    bs_obj = BeautifulSoup(pageString, "html.parser")

    journal = ""
    cit = bs_obj.find("div", {"class":"cit"})
    try:
        journal = cit.text.split(" doi")[0]
    except Exception:
        journal = cit.text
        print("error")


    rprt_all = bs_obj.find("div", {"class":"rprt_all"})
    title = rprt_all.find("h1").text

    authors = []
    try:
        afflist = bs_obj.find("div", {"class":"afflist"})
        dds = afflist.findAll("dd")
        authors = [dd.text for dd in dds]
    except Exception:
        print("error authors")

    abstract = ""
    try:
        abstr = bs_obj.find("div", {"class":"abstr"})
        abstract = abstr.find("div").text
    except Exception:
        print("error abstract")

    keywords = ""
    try:
        keywords = bs_obj.find("div", {"class":"keywords"}).text
        keywords = keywords.split("; ")
    except Exception:
        print("keywords error")
    return {"journal": journal, "title":title, "authors":authors, "abstract":abstract, "keywords":keywords}