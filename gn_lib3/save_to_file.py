
def saveToFile(list, fileLocationName):
    file = open(fileLocationName, "w+")

    for item in list:
        file.write(str(item['name'])+"\n")
    file.close()