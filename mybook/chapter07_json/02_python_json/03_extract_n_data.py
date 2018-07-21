import json
json_str = '[{"name":"kyeongrok", "age":"32"}, {"name":"bomi", "age":"25"}]'
json_obj = json.loads(json_str)

print(json_obj[1])
print(json_obj[0:2])



'''
list기준으로는 item이 두개. 왜냐하면 중괄호가 두개이기 때문. 그리고 ,컴마로 구분 되어 있다.

'''

'''
print(json_obj[2])
IndexError: list index out of rangeㅆ
list는 0번 index부터 시작합니다.
'''