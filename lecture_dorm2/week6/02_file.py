file = open("./hello.txt", "w+")
list = [
    {"name":"hello"},
    {"name":"world"}
]
for item in list:
    file.write(item['name']+"\n")
file.close()