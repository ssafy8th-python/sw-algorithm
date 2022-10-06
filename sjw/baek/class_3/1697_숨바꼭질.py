# 1697 숨바꼭질
# 주소: https://www.acmicpc.net/problem/1697

# 제출한 답
import sys
from collections import deque  # 덱 안쓴경우: 516ms 덱 쓴경우: 156ms
input = sys.stdin.readline


def superSubin(v, g):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        v = q.popleft()
        if v == g:
            return visited[v]
        if 0 <= v + 1 <= 100001 and not visited[v + 1]:
            q.append(v + 1)
            visited[v + 1] = visited[v] + 1
        if 0 <= v - 1 <= 100001 and not visited[v - 1]:
            q.append(v - 1)
            visited[v - 1] = visited[v] + 1
        if 0 <= v * 2 <= 100001 and not visited[v * 2]:
            q.append(v * 2)
            visited[v * 2] = visited[v] + 1


n, k = map(int, input().split())
visited = [0] * 100002
print(superSubin(n, k) - 1)
