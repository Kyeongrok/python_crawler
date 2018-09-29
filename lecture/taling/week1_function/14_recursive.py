def multiple(n, a):
    if(n == 1): return a
    return multiple(n-1, a) + a

result = multiple(4, 5)
print(result)
