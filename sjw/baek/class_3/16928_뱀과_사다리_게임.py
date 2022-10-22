# 16928 뱀과 사다리 게임
# 주소: https://www.acmicpc.net/problem/16928

# 제출한 답 88ms
import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    visited = [-1] * 110
    q = deque()
    q.append(1)
    visited[1] = 0
    while q:
        v = q.popleft()
        if v >= 100:
            return visited[v]
        else:
            for i in graph[v]:
                if visited[i] == -1:
                    q.append(i)
                    visited[i] = visited[v] + 1


n, m = map(int, input().split())
graph = [[i + 1, i + 2, i + 3, i + 4, i + 5, i + 6] for i in range(101)]
for _ in range(n + m):
    x, y = map(int, input().split())
    graph[x] = [y + 1, y + 2, y + 3, y + 4, y + 5, y + 6]

print(bfs())


# 수정한 답 99ms
import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    visited = [-1] * 101
    q = deque()
    q.append(1)
    visited[1] = 0
    while q:
        v = q.popleft()
        if v == 100:
            return visited[v]
        else:
            for i in range(1, 7):
                tmp = graph[v] + i
                if 0 < tmp <= 100 and visited[tmp] == -1:
                    q.append(tmp)
                    visited[tmp] = visited[v] + 1


n, m = map(int, input().split())
graph = [i for i in range(101)]
for _ in range(n + m):
    x, y = map(int, input().split())
    graph[x] = y

print(bfs())


# 다른 답
import sys

N, M = map(int, sys.stdin.readline().split())

area = [i for i in range(101)]
visited = [0] * 101
for i in range(N + M):
    s, e = map(int, sys.stdin.readline().split())
    area[s] = e

q = [(1, 0)]  # (현재 위치, 지금까지 이동한 횟수)

while q:
    cur, times = q.pop(0)
    if cur == 100:
        print(times)
        break

    else:
        for i in range(1, 7):
            temp_cur = cur + i
            if 1 <= temp_cur <= 100 and not visited[temp_cur]:
                visited[temp_cur] = 1
                q.append((area[temp_cur], times + 1))

