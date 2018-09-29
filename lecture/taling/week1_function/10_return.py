# return 함수 실행의 결과를 돌려줍니다.
# 리턴, 반환, 돌려준다
def plus(val_a, val_b):
    return val_a + val_b

def minus(val_a, val_b):
    return val_a - val_b

def multiple(val_a, val_b):
    return val_a * val_b

def divide(val_a, val_b):
    return val_a / val_b

# k5
result = plus(10, 20)
print("=>", result)

result_minus = minus(10, 20)
print("=>", result_minus)

result_multiple = multiple(10, 20)
print("=>", result_multiple)

result_divide = divide(10, 20)
print("=>", result_divide)
