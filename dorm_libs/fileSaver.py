def saveHello():
    file = open("./hello.html", "w+", encoding="utf-8")
    file.write("hello")
    file.close()

# "./hello.html"
def save(fileLocationName, contents):
    file = open(fileLocationName, "w+")
    file.write(contents)
    file.close()