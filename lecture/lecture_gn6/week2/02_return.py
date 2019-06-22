def plus(val1, val2):
    result = val1 + val2
    return result

def minus(val1, val2):
    result = val1 - val2
    return result

def multiple(val1, val2):
    # 데이터 뽑아내는 여러줄의 로직
    return val1 * val2

def divide(val1, val2):
    return val1 / val2

# 함수 호출
plusResult = plus(10, 20)
minusResult = minus(10, 20)
multipleResult = multiple(10, 20)
divideResult = divide(10, 20)

print(plusResult)
print(minusResult)
print(multipleResult)
print(divideResult)

# 10 * 20 / 80 - 70
# 10 / 20 - 80 * 70
# 1 -> 잔머리형
print(10 * 20 / 80 - 70)

# 2 -> 프론티어
def someCalc(val1, val2, val3, val4):
    return val1 * val2 / val3 - val4

print(someCalc(10, 20, 80, 70))

# 3 -> 로지컬
result1 = multiple(10, 20)
result2 = divide(result1, 80)
result3 = minus(result2, 70)

print(result3)

# 4 -> 만능형
result4 = minus(divide(multiple(10, 20), 80), 70)
print(result4)
