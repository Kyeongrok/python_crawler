import random

file_name = "./save_line.txt"
f1 = open(file_name, mode='w+')
for item in range(0, 10):
    f1.write(str(random.randint(1, 100)) + "\n")
f1.close()