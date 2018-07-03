import json

file = open("./exchange_rate.json","r", encoding="utf-8")
jjson = json.loads(file.read())

# print(jjson)

print(jjson['BTCKRW']['coinone']['last'])
print(jjson['LTCKRW']['coinone']['last'])
print(jjson['BCHKRW']['coinone']['last'])
print(jjson['EOSKRW']['coinone']['last'])
print(jjson['ETHKRW']['coinone']['last'])