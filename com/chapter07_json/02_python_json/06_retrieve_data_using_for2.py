import json
json_str = '[{"name":"kyeongrok", "age":"32"}, {"name":"bomi", "age":"25"}]'
json_obj = json.loads(json_str)

for student in json_obj:
    print(student['name'])