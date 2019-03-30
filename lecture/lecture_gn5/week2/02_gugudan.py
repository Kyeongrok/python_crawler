# 2 * 1 = 2 를 출력하는 gugudan이라는 이름의 함수를 만들고
# 2 * 1 = 2 를 콘솔에 출력 해보세요.
def multiple(val1, val2):
    return val1 * val2

def gugudan(dan):
    # 반복문 이용해서 9번 출력 해보세요
    for num in range(1, 10):
        print("{} * {} = {}".format(dan, num, dan * num))
        # 2 * 2 = 4
        # 2 * 3 = 6

for dan in range(2, 10):
    gugudan(dan)
# 2단, 3단 동시에

