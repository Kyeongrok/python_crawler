from bs4 import BeautifulSoup

def parse(string):
    bsObj = BeautifulSoup(string, "html.parser")
    section = bsObj.find("section", {"class":"M18_potlete_cont1"})
    print(section)
