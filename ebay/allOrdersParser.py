fileName = "./allorders.html"
def printLineByLine(file_path):
    with open(file_path, 'rt', encoding='utf-8') as f:
        line = f.readline()
        return line


result = printLineByLine(fileName)
print(result)