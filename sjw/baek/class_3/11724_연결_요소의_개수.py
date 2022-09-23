# 11724 연결 요소의 개수
# 주소: https://www.acmicpc.net/problem/11724

# 제출한 답
import sys
input = sys.stdin.readline


def dfs(k):
    global cnt
    s = [k]
    visited[k] = 1

    while s:
        v = s.pop()

        for w in g[v]:
            if not visited[w]:
                s.append(w)
                visited[w] = 1
    cnt += 1


n, m = map(int, input().split())

g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [0] * (n + 1)

cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)

print(cnt)
