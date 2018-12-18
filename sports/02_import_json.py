import json

file = open("./bet365_prematch_odds.json")
jsonObj = json.loads(file.read())


result = jsonObj['results'][0]
print(result)


