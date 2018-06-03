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