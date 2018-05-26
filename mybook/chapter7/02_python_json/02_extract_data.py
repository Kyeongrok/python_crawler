import json
json_str = '[{"name":"kyeongrok", "age":"32"}]'
json_obj = json.loads(json_str)

print(json_obj)
print(json_obj[0])

'''
뭐가 다를까요?
[]가 없습니다.
'''