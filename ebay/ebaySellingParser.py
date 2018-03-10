from bs4 import BeautifulSoup
# 파서에 들어가야 하는 기능?
# 문자열에서 필요한 것만 뽑아내는 것

# 원하는 텍스트를 뽑아오는 방법
fileName = "./hello.txt"
def printLineByLine(file_path):
    with open(file_path, 'rt', encoding='utf-8') as f:
        line = f.readline()
        return line


result = printLineByLine(fileName)
soup = BeautifulSoup(result, 'html.parser')
summary_bar = soup.find("div",{"class":"summary-bar"})

print(summary_bar)