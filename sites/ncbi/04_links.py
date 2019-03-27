from bs4 import BeautifulSoup

def getLinks(pageStr):
    bs_obj = BeautifulSoup(pageStr, "html.parser")
    rprts = bs_obj.findAll("div", {"class":"rprt"})
    links = []
    for item in rprts:
        atag = item.find("a")

        links.append(atag["href"].replace("/pubmed/", ""))

    return links

links = []
for num in range(2, 194):
    print(num)
    file = open("./links_page/"+str(num) + ".html")
    result = getLinks(file.read())
    links = links + result

links.sort()
file = open("./links.txt", "w+")
for link in links:
    file.write(link + "\n")
