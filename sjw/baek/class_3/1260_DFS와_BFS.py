# 1260 DFS와 BFS
# 주소: https://www.acmicpc.net/problem/1260

# 제출한 답
import sys
input = sys.stdin.readline

def dfs(k):
    result = []
    visited = [0] * (n + 1)
    st = [k]
    while st:
        v = st.pop()
        if not visited[v]:
            result.append(v)
        visited[v] = 1
        for i in n_lst[v][::-1]:
            if not visited[i]:
                st.append(i)

    return result


def bfs(k):
    result = []
    visited = [0] * (n + 1)
    q = [k]
    while q:
        v = q.pop(0)
        if not visited[v]:
            result.append(v)
        visited[v] = 1
        for i in n_lst[v]:
            if not visited[i]:
                q.append(i)

    return result


n, m, v = map(int, input().split())

n_lst = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    n_lst[a].append(b)
    n_lst[b].append(a)

for lst in n_lst:
    lst.sort()


print(*dfs(v))
print(*bfs(v))

