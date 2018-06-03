import json
json_str = '[{"name":"kyeongrok", "age":"32"}, {"name":"bomi", "age":"25"}]'
json_obj = json.loads(json_str)

print(json_obj[0])
print(json_obj[0]['name'])
print(json_obj[0]['age'])