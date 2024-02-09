# 13549 숨바꼭질 3
# 주소: https://www.acmicpc.net/problem/13549

# 제출한 답1
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [1e10] * 100001

q = deque([N])
visited[N] = 0
while q:
    v = q.popleft()
    if v == K:
        print(visited[v])
        break
    for d in [1, -1, 2]:
        if d == 2:
            x = v * d
            time = 0
        else:
            x = v + d
            time = 1
        if 0 <= x <= 100000 and visited[x] > visited[v] + time:
            visited[x] = visited[v] + time
            q.append(x)
