# 최소 생산 비용
'''
1
73 21 21
11 59 40
24 31 83
'''

def dfs(k, state):    # 깊이, 선택 위치, 더한값
    global minV
    if k == n:
        if minV > state:
            minV = state
        return

    if state > minV:
        return

    for i in range(n):  # 한 번 간곳은 다시 가지 않도록
        if visited[i]:
            visited[i] = False
            dfs(k+1, state+arr[k][i])
            visited[i] = True

T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    visited = [True]*n
    minV = 1000000000
    dfs(0, 0)
    print(f'#{tc} {minV}')

