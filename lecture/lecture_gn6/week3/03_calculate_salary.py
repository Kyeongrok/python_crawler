# 연봉 계산기를 만들어 보세요
# 어떻게 계산하냐면 연차 * 0.9
# 함수 이름 getSalary
# parameter이름은 year

def getSalary(year):
    return year * 9000000

mySalary = getSalary(7)
print(mySalary)

def getVat(amount):
    return amount * 0.1

myVat = getVat(mySalary)
print("myVat:", myVat)
