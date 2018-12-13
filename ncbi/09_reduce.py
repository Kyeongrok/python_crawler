import glob
import json

fileList = glob.glob("/Users/kyeongrok/Desktop/json_results/*.json")

list = []

for fileName in fileList:
    file = open(fileName)
    jsonObj = json.loads(file.read())
    jsonObj['id'] = fileName.replace(".json", "").replace("/Users/kyeongrok/Desktop/json_results/","")
    list.append(jsonObj)
    file.close()

print(len(list))
open("./result2.json", "w+").write(json.dumps(list))