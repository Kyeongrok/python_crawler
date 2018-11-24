def multiple(a,b):
    return a*b

for a in range (2,10):
    for number in range(1,10):
        print(a,"x", number, "=", multiple(a, number))
