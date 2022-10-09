# 종이의 개수
import sys
input = sys.stdin.readline

def divid(r, c, n):     # 시작r,c 변의 길이
    global minus, plus, zero
    if n == 1:
        if arr[r][c] == -1:
            minus += 1
        elif arr[r][c] == 0:
            zero += 1
        elif arr[r][c] == 1:
            plus += 1
        n *= 3
        return

    tmp = set()
    for i in range(r, r+n):
        for j in range(c, c+n):
            tmp.add(arr[i][j])
    tmp = list(tmp)
    if len(tmp) == 1:
        if tmp[0] == -1:
            minus += 1
        elif tmp[0] == 0:
            zero += 1
        elif tmp[0] == 1:
            plus += 1
        return

    divid(r,c,n//3) # (1)
    divid(r+n//3,c,n//3) # (2)
    divid(r+2*(n//3),c,n//3) # (3)
    divid(r,c+n//3,n//3) # (4)
    divid(r,c+2*(n//3),n//3) # (5)
    divid(r+n//3,c+n//3,n//3) # (6)
    divid(r+n//3,c+2*(n//3),n//3) # (7)
    divid(r+2*(n//3),c+n//3,n//3) # (8)
    divid(r+2*(n//3),c+2*(n//3),n//3) # (9)



n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
minus, zero, plus = 0,0,0
divid(0,0,n)
print(minus)
print(zero)
print(plus)