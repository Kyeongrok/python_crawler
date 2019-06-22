# 2 * 1 = 2 를 console에 출력 해보세요.
# printGugudan() 이라는 함수를 만들어서 출력해보세요.

# 함수 선언
def printGugudan(dan):
    for num in range(1, 9 + 1):
        print(dan, "*", num,"=", dan * num)
    print("-------------")


# 함수 호출
for dan in range(2, 9 + 1):
    printGugudan(dan)

# 2단, 3단 동시에 출력하기
