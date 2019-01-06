# 1 to 20
def printNumbers(pageNum):
    list = []
    for num in range(1, 20 + 1):
        list.append(num * pageNum)
    return list

# 1 page to 17 page
for num in range(1, 18):
    print(printNumbers(num))

