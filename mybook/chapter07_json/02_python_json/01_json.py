import json
json_str = '{"name":"kyeongrok", "age":"32"}'
json_obj = json.loads(json_str)

print(json_obj)







'''
# list기준으로 item은 한개이다.
왜냐하면 {}중괄호가 1쌍이므로.

{}는 json object이다.
# json 오브젝트 기준으로는 item이 2개이다.
왜냐하면 ,컴마로 구분 하기 때문
'''
