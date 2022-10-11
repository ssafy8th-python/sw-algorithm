from collections import deque

def bfs(lst):
    q = deque([lst[0]])
    visited = [False] * (N + 1)
    visited[lst[0]] = True
    res = 1
    while q:
        curV = q.popleft()

        for node in G[curV]:
            if not visited[node] and node in lst:
                visited[node] = True
                q.append(node)
                res += 1

    return res


def nCr(N, r, s):
    global minV
    if r == 0:
        a = bfs(lst)
        tmp = set(lst)
        tmp = all_lst - tmp
        tmp = list(tmp)
        b = bfs(tmp)
        if a + b == N:
            res1 = 0
            res2 = 0
            for index in lst:
                res1 += weight[index]

            for index in tmp:
                res2 += weight[index]

            res = abs(res1 - res2)
            if minV > res:
                minV = res

        return

    for i in range(s, N - r + 1):
        lst[r-1] = i + 1
        nCr(N, r-1, i + 1)


N = int(input())

weight = [0] + list(map(int, input().split()))

G = [[] for _ in range(N+1)]

all_lst = [i for i in range(1, N + 1)]
all_lst = set(all_lst)
minV = 1000

for i in range(1, N+1):
    arr = list(map(int, input().split()))

    for num in arr[1:]:
        G[i].append(num)

for i in range(1, N//2 + 1):
    lst = [0] * i
    nCr(N, i, 0)

if minV == 1000:
    print(-1)
else:
    print(minV)