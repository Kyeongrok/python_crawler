import glob
import json

fileList = glob.glob("/Users/kyeongrok/Desktop/json_results/*.json")

list = []

for fileName in fileList:
    file = open(fileName)
    list.append(json.loads(file.read()))
    file.close()

print(len(list))
open("./result2.json", "w+").write(json.dumps(list))