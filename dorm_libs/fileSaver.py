def saveHello():
    file = open("./1.html", "w+", encoding="utf-8")
    file.write("hello")
    file.close()

# "./1.html"
def save(fileLocationName, contents):
    file = open(fileLocationName, "w+")
    file.write(contents)
    file.close()