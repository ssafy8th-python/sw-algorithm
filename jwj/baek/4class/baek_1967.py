import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def dfs(start, s):
    global maxNode

    check = True

    for end_node, weight in graph[start]:
        if not visited[end_node]:
            check = False
            visited[end_node] = True
            dfs(end_node, s + weight)

    if check:
        if maxNode[1] < s:
            maxNode[0] = start
            maxNode[1] = s


n = int(input())

graph = [[] for _ in range(n + 1)]

maxNode = [0, 0]

for _ in range(n-1):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))


visited = [False] * (n + 1)
visited[1] = True

dfs(1, 0)

visited = [False] * (n + 1)
visited[maxNode[0]] = True
dfs(maxNode[0], 0)

print(maxNode[1])
