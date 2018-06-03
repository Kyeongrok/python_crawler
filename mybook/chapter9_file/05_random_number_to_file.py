import random

file_name = "./random_number.txt"
f1 = open(file_name, mode='w+')
for item in range(1, 1000+1):
    f1.write(str(random.randint(1, 100)) + "\n")
f1.close()
print("파일 저장이 완료 되었습니다. 같은 폴더에 {}를 찾아보세요.".format(file_name))

