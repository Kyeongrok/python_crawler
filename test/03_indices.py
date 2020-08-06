A = [0, 3, 3, 7, 5, 3, 11, 1]
A = [1, 4, 7, 3, 3, 5]
def solution(A):
    minDistance = len(A) - 1
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            cnt = 0
            large = max(A[i], A[j])
            small = min(A[i], A[j])
            for num in range(small+1, large):
                if num in A:
                    cnt += 1

            if cnt == 0 and small != large:
                distance = abs(i - j)
                if distance < minDistance:
                    minDistance = distance
    return minDistance
print(solution(A))