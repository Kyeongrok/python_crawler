# return 함수를 호출한 곳으로 결과를 보내주는 것

# plus라는 이름의 함수를 만들고
# 매개변수 두개를 추가 해보세요
def plus(val1, val2):
    # val1과 val2를 더한 값을 출력 해보세요
    return val1 + val2

plus(10, 20)

def minus(val1, val2):
    return val1 - val2

minus(10, 20)

def multiple(val1, val2):
    return val1 * val2

def divide(val1, val2):
    return val1 / val2

multiple(10, 20)
divide(10, 20)

# 30 * 40 - 70 / 60 + 100

print(30 * 40 - 70 / 60 + 100)
result1 = multiple(30, 40)
result2 = divide(70, 60)
result3 = minus(result1, result2)
result4 = plus(result3, 100)

print("result1:", result1)
print("result2:", result2)
print("result3:", result3)
print("result4:", result4)