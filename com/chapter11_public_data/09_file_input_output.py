f = open("C:\json_data\sample_data.txt", 'w')
data = "easy_python_crawler"
f.write(data)
f.close()

f = open("C:\json_data\sample_data.txt", 'r')
for str in f.readlines():
    print(str)
f.close()
