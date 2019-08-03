import json
# json
result = [
    {"name":"coffee1", "price":10000},
    {"name":"coffee2", "price":20000}
]

file = open("./jsonexam.json", "w+")
file.write(json.dumps(result))

# naver shopping 1 ~ 10 -> [{}, {}]
# file로 저장 해보세요. coffee.json

