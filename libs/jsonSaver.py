import json

def save(content, fileName):
    file = open(fileName, "w+")
    file.write(json.dumps(content))