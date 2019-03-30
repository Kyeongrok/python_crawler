# plus라는 이름의 함수를 만들어 보세요
# 파라메터는 val1, val2
# 두개의 입력받은 값을 더한 결과를 리턴하는 함수를 만들어서
# 10 + 20을 콘솔에 출력 해보세요.

def plus(val1, val2):
    result = val1 + val2
    return result

def minus(val1, val2):
    return val1 - val2

def multiple(val1, val2):
    return val1 * val2

def divide(val1, val2):
    return val1 / val2

result = plus(10, 20)
print(result)

print(minus(10, 20))

# (10 + 20) * (30 - 40) / 20
result1 = plus(10, 20)
result2 = minus(30, 40)
result3 = multiple(result1, result2)
result4 = divide(result3, 20)
print("result4:", result4)

result5 = divide(multiple(plus(10, 20), minus(30, 40)), 20)
print("result5:", result5)

def something(v1, v2, v3, v4, v5):
    return (v1 + v2) * (v3 - v4) / v5

print("sth:", something(10, 20, 30, 40, 20))