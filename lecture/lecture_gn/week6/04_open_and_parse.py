import libs.jolse.jolse_parser as parser

file = open("./jolse_02.html")
result = parser.parse(file.read())
print(len(result))

savedFile = open("./jolse_02.csv", "w+")
for item in result:
    savedFile.write(str(item['name']) + "\n")