import json

file = open("./gae.json")
bible = json.loads(file.read())
print(len(bible))

for ee in bible:
    print(ee)
