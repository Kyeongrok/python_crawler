from bs4 import BeautifulSoup



fileName = "./eachPage1.html"
def getFileString(file_path):
    with open(file_path, 'rt', encoding='utf-8') as f:
        line = f.read()
        return line

file_string = getFileString(fileName)
bsObj = BeautifulSoup(file_string, "html.parser")
print(bsObj)