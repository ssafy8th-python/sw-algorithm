import sys

sys.stdin = open("input_4881.txt", "r")

def dfs(i, sumV):
    global minV
    if i == n:
        if sumV < minV:
            minV = sumV
    if sumV >= minV:
        return

    for j in range(n):
        if check[j]:
            print(check)
            check[j] = False
            dfs(i+1, sumV + arr[i][j])
            check[j] = True

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    check = [True for _ in range(n)]
    minV = 100
    sumV = 0
    dfs(0, sumV)
    print(f'#{tc} {minV}')