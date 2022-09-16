import sys
input = sys.stdin.readline


def dfs(s, val):
    global max_val
    global max_node
    check = True
    visited[s] = True

    for v, w in tree[s]:
        if not visited[v]:
            dfs(v, val + w)
            check = False

    if check:
        if max_val < val:
            max_val = val
            max_node = s


V = int(input())

tree = [[] for _ in range(V+1)]

for _ in range(V):
    arr = list(map(int, input().split()))
    start = arr[0]

    for idx in range(1, len(arr)-1, 2):
        tree[start].append((arr[idx], arr[idx+1]))
        tree[arr[idx]].append((start, arr[idx+1]))

visited = [False] * (V + 1)
visited[1] = True

max_val = 0
max_node = 0

dfs(1, 0)

visited = [False] * (V + 1)
visited[max_node] = True

dfs(max_node, 0)

print(max_val)
