# 최소합
import sys
sys.stdin = open("sample_input (7).txt","r")
def f(k, r, c, midSum):
    global result

    if result <= midSum:
        return

    if r == n-1 and c == n-1:
        if result > midSum:
            result = midSum
        return

    if r+1 < n:
        f(k+1, r+1, c, midSum+arr[r+1][c])

    if c+1 < n:
        f(k+1, r, c+1, midSum+arr[r][c+1])

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    midSum = arr[0][0]
    mn =100000
    result = mn

    f(0,0,0,midSum)
    print(f'#{tc} {result}')