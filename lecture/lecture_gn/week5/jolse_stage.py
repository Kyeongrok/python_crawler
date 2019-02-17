import libs.jolse.jolse_parser as parser

def getProdList(fileName):
    file = open(fileName, encoding="utf-8")
    str = file.read()
    prodList = parser.parse(str)
    return prodList

prodList1 = getProdList("./troublecare_1.html")
prodList2 = getProdList("./troublecare_2.html")

mergedList = prodList1 + prodList2

file = open("./product_info.csv", "w+")
for item in mergedList:
    file.write(item['name'] + "@" + item['price'] + "\n")
