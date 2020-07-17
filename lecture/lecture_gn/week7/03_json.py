import json
list = [
    {"title":"hello", "blogger":"world"}
]
file = open("./data_file.json", "w+")
file.write(json.dumps(list))

