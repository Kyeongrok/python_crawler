# 구구단 2단 출력하기
# 2 * 1 = 2를 console에 출력 해보세요.
# 2 * 9 = 18까지 출력 해보세요
def printGugudan(dan):
    for num in range(1, 9 + 1):
        print(dan, "*", num, "=", dan * num) # 20
    print("-------------")

for dan in range(2, 100000 + 1):
    printGugudan(dan)

# 1. 여기에서 함수 pringGugudan()은 몇번줄까지일까요? 9
# 2. 6번줄
# 3.

# type 타입 형 문자형, 숫자형
#"1" => 문자  계산 못함
#1 => 숫자 계산 가능

