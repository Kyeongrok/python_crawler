import re
import os
from libs.jsonFileSaver import save


pattern = "[가-힣]{1,2}[0-9]{1,3}:[0-9]{1,3} "
def fileToList(fileName):
    file = open(fileName)
    lines = file.readlines()

    result = []
    for line in lines:
        try:
            index = re.search(pattern, line).group(0)
            replaced = re.sub(pattern, "", line)
            statement = {"fileName":fileName, "index":index, "text":replaced.replace("\n", "")}
            result.append(statement)
        except Exception as e:
            print(line)
            print("---error---", e)

    return result

result = {}
for root, dirs, files in os.walk("./books/"):
    for filename in files:
        lines = fileToList("./books/{}".format(filename))
        result[filename] = lines

save(result, "gae.json")