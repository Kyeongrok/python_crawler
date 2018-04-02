from bs4 import BeautifulSoup



fileName = "./eachPage1.html"
def getFileString(file_path):
    with open(file_path, 'rt', encoding='utf-8') as f:
        line = f.read()
        return line

file_string = getFileString(fileName)
bsObj = BeautifulSoup(file_string, "html.parser")

tbody = bsObj.find("tr", {"class":"shreskin-edit-sales-record-buyer-details"}).find("table").find("tbody").find("table").find("tbody")

trs = tbody.findAll("tr")

print(trs[0].findAll("td")[1].find("b").text)


