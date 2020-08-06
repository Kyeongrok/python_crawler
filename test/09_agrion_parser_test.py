from libs.agrion.parser import parse

file = open('hello.html')
file_content = file.read()
res = parse(file_content)
#
print(res)