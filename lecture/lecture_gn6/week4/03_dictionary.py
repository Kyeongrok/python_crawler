# name을 추가해보세요
companyInfo = {"price":30600, "employee":30000, "name":"코오롱생명~"}

print(companyInfo)


numList = [1, 2] #numList에 숫자 2를 추가 해보세요
numList.append(3)
print(numList)

#sk하이닉스를 companyInfoList에 추가 해보세요 68400원
companyInfoList = [{"name":"코오롱~", "price":30600}, {"name":"sk하이닉스","price":68400}]
companyInfoList.append({"name":"신한지주", "price":44400})
print(companyInfoList)

# list는 여러개의 정보를 표현 합니다
# dictionary는 한개의 정보를 표현 합니다

for num in numList:
    print(num)

# companyInfoList에 있는 회사 정보를 하나씩 뽑아서 출력해보세요
def getVat(price):
    return price * 0.1

for companyInfo in companyInfoList:
    # 회사 이름만 출력 하려면 어떻게 해야 할까요?
    print(companyInfo["price"] * 0.1)

# vat구하는 함수를 실행해서 이 회사들의 한주당 vat를 출력해보세요.

