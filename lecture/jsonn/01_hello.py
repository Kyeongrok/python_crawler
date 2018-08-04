import requests
import json

f = open("./sample_data.json", 'r', encoding='utf-8')
data = f.read()

json_str = json.dumps(data)
json_obj = json.loads(json_str)

print(type(json_obj))
print(json_obj)
