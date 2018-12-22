## File
```python
with open("./hello.txt", mode="w+") as f:
    f.write("hello \n")
```
파일에 데이터 저장하기


```python
f1 = open("./hello.txt", mode='r')
lines = f1.readlines()

print(lines)
```

여러줄 저장하기
```python
import random

file_name = "./save_line.txt"
f1 = open(file_name, mode='w+')
for item in range(0, 10):
    f1.write(str(random.randint(1, 100)) + "\n")
f1.close()
```
