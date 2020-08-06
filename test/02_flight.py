N = 2
S = "1A 2F 1C"

def countFamily(A):
    if A[1] == 0 and A[2] == 0 and A[3] == 0 and A[4] == 0 and A[5] == 0 and A[6] == 0 and A[7]==0 and A[8]==0:
        return 2
    elif A[3] == 0 and A[4] == 0 and A[5] == 0 and A[6] == 0:
        return 1
    elif A[1] == 0 and A[2] == 0 and A[3]==0 and A[4]==0:
        return 1
    elif A[5] == 0 and A[6] == 0 and A[7]==0 and A[8]==0:
        return 1
    return 0

def solution(N, S):
    cnt = 0
    seats = [[0] * 10 for i in range(N)]
    map = {
        "A":0, "B":1, "C":2, "D":3, "E":4, "F":5,
        "G":6, "H":7, "J":8, "K":9
    }
    seatsAddrs = S.split(" ")
    if S != "":
        for seatsAddr in seatsAddrs:
            seats[int(seatsAddr[0]) - 1][map[seatsAddr[1]]] = 1

    for seat in seats:
        cnt += countFamily(seat)

    return cnt

print(solution(N, S))
print(solution(1,""))