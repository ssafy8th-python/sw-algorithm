# 동철이의 일 분배
import sys
sys.stdin = open("input (13).txt","r")
'''
1
3
13 0 50
12 70 90
25 60 100
'''

def dfs(k, state):
    global mx
    if k == n:
        if mx < state:
            mx = state
        return

    if state <= mx:
        return

    for i in range(n):
        if visited[i]:
            visited[i] = False
            dfs(k+1, state*(arr[k][i]/100))
            visited[i] = True

T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [True]*n
    mx = 0
    dfs(0, 1)
    print(f'#{tc} {mx*100:.6f}')
