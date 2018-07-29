# f라는 함수 선언
def f(param1):
    return param1 + 10

def g(param1):
    return param1 * 20

# 합성함수
# f o g(x) = f(g(x))
# f o g(10) = 210
print(f(g(10)))
