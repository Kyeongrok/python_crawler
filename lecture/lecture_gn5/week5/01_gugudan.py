# 구구단 2단을 출력하는 함수를 만들고
# 구구단 2단을 출력 해보세요
# 단이 끝날 때마다 구분선을 넣어보세요.

def gugudan(dan):
    for num in range(1, 9 + 1):
        print("{} * {} = {}".format(dan, num, dan * num))

for dan in range(2, 9 + 1):
    gugudan(dan)
    print("---------------")
