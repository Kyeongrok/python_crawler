A = [3, 2, -2, 5, -3]

def solution(A):
    positive = []
    negative = []
    result = []

    for n in A:
        if n > 0:
            positive.append(n)
        elif n < 0:
            negative.append(n)

    for ne in negative:
        if abs(ne) in positive:
            result.append(ne)

    if len(result) == 0:
        return 0
    else:
        result.sort()
        return abs(result[0])

