splitted = "hello world bye".split(" ")

print(splitted[1])

targetString = "aa=19"
start = len(targetString) - 3
end = len(targetString)
result = targetString[start:end]

print(result.replace("=", ""))
