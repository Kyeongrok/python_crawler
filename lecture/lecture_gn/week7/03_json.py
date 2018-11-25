import json
list = [
    {"title":"hello", "blogger":"world"}
]
file = open("./data.json", "w+")
file.write(json.dumps(list))

