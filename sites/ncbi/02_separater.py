import json
file = open("./links.txt")

lines = file.readlines()

list = []
for line in lines:
    list.append(line.replace("\n", ""))

list.sort()

file2 = open("./links2.json", "w+")
file2.write(json.dumps(list))
