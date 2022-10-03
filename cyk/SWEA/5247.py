# 연산
from collections import deque

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == M:
            return visited[v]
        for calc in [v+1,v-1,v*2,v-10]:
            if 0< calc <= 1000000 and visited[calc] == 0 :
                visited[calc] = visited[v] + 1
                q.append(calc)

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    max = 1000001
    visited = [0]*max
    print(f'#{tc} {bfs(N)}')