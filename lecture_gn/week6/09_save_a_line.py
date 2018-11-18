file = open("./hello.csv", "w+")
file.write("hello" + "\n")
file.write("bye" + "\n")

list = ["welcome", "glad"]
for item in list:
    file.write(item + "\n")
