import json

file = open("./exchange_rate.json","r", encoding="utf-8")
jjson = json.loads(file.read())

# print(jjson)

print(jjson['BTCKRW']['chapter13_coinone']['last'])
print(jjson['LTCKRW']['chapter13_coinone']['last'])
print(jjson['BCHKRW']['chapter13_coinone']['last'])
print(jjson['EOSKRW']['chapter13_coinone']['last'])
print(jjson['ETHKRW']['chapter13_coinone']['last'])