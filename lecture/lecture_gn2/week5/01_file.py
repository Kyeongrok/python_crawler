import json
jsonObj = {"name":"다우니", "price":"12000"}

file = open("./product.json", "w+")
file.write(json.dumps(jsonObj))