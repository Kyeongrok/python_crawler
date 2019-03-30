# 2단을 출력하는 printGugudan함수를 만들고
# 2단을 출력 해보세요.

def printDan():
    for dan in range(2, 10):
        for num in range(1, 10):
            print(dan, "*", num, "=", dan * num )

printDan()

