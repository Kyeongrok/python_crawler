# salary 연봉을 계산해주는 함수를 만들어 보세요
# 연차 * 900만원
# 연차를 넣으면 연봉을 return 해주는 기능
# 함수이름 : getSalary()
def getSalary(year):
    return year * 9000000

# getVAT() 금액을 받아서 * 0.1한 결과를 return
def getVAT(price):
    return price * 0.1

salary = getSalary(7)
vat = getVAT(salary)
print("salary:", salary)
print("vat:", vat)


# f(x) = x + 1
# g(y) = y * 10

# x에 20을 넣으면 어떻게 될까요?

# 위 두 함수를 만들고 20을 넣으면 어떻게 되는지
# console에 출력 해보세요.

def getF(x):
    return x + 1
def getG(y):
    return y * 10

def gOf(x):
    return (x + 1) * 10

resultFx = getF(20)
resultGy = getG(resultFx)
print("resultFx:",resultFx)
print("resultGy:",resultGy)

# g o f(x) =
print(getG(getF(20)))
