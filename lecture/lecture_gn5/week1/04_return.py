def plus(val1, val2):
    result = val1 + val2
    return result

result = plus(10, 20)
print(result)

# minus 10 - 20의 결과가 콘솔에 나오게 해주세요
# multiple, divide 10, 20
def minus(val1, val2):
    result = val1 - val2
    return result

result = minus(10, 20)
print(result)

def multiple(val1, val2):
    result = val1 * val2
    return result

def divide(val1, val2):
    return val1 / val2

print(multiple(10, 20))
print(divide(10, 20))

# (10 + 20) - (30 * 40)

# 방법1
def somethingProcess(v1, v2, v3, v4):
    return (v1 + v2) - (v3 * v4)
print(somethingProcess(10, 20, 30, 40))

# 방법2
result1 = plus(10, 20)
result2 = multiple(30, 40)
result3 = minus(result1, result2)
print(result3)

# 방법3
print(minus(plus(10, 20),multiple(30, 40)))