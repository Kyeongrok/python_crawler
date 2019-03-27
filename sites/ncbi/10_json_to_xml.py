from json import loads
from dicttoxml import dicttoxml

def convertJsonToXml(fromFileName, toFileName):
    json_obj = loads(str(open(fromFileName).read()))
    print(type(json_obj))

    xml = dicttoxml(json_obj)

    file = open(toFileName, "w+")
    file.write(str(xml))
    file.close()

location = "/Users/kyeongrok/Desktop/"
convertJsonToXml(location +"result.json",location+"result_xml.json")