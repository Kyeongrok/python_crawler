from json import loads
from dicttoxml import dicttoxml


json_obj = loads(str(open("/Users/kyeongrok/Desktop/result.json").read()))
print(type(json_obj))

xml = dicttoxml(json_obj)

file = open("/Users/kyeongrok/Desktop/result_xml.json", "w+")
file.write(str(xml))
file.close()
