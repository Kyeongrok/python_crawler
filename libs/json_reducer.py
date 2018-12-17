import glob
import json

# json 특정 위치에 있는 json파일을 모두 열어 하나로 합친다.
def collectToOneFile(targetFileName, location):
    fileList = glob.glob(location+"*.json")
    list = []
    for fileName in fileList:
        file = open(fileName)
        jsonObj = json.loads(file.read())
        jsonObj['id'] = fileName.replace(location+".json", "").replace(location,"")
        list.append(jsonObj)
        file.close()

    print(len(list))
    open(targetFileName, "w+").write(json.dumps(list))
