# 구구단 2단 출력하는 함수를 만들고 실행 해보세요
# 유투브 '파이썬 크롤링'검색
# 단톡방 링크 스크롤 스크롤

# 구구단 2단
# 구구단 3단
# parameter
def gugudan(dan):
    for number in range(1, 9+1):
        print("{} * {} = {}".format(dan, number,dan*number))

# 2단 ~ 9단 동시에
for dan in range(2, 9+1):
    print("-------------------")
    print(dan)
    gugudan(dan)



