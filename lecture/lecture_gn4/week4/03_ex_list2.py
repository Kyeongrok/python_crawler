# 1부터 20까지 들어있는 list를 만들어 주세요
nums = list(range(1, 21))
# multiple이라는 이름의 함수를 만들어 주세요.
# 함수의 기능은 'hello'를 출력 하는 것입니다.
# num이라는 parameter를 추가 해주세요.
# 받은 num을 return하는 기능을 추가 해주세요.
# multiple이 받은 parameter에 2를 곱해서 리턴하게 바꿔주세요.
def multiple(num):
    return num * 2

# 위에서 만든 20개의 숫자에 각각 2를 곱한 결과를 출력해주세요.
# 곱할때는 앞에서 만든 함수를 이용해주세요.
for num in nums:
    result = multiple(num)
    print(result)

print("nums:", len(nums))

print(list(range(1, 10000)))