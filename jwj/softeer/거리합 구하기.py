import sys
sys.setrecursionlimit(10**7)


def dfs1(current, parent):

    for child, weight in graph[current]:
        if child != parent:
            dfs1(child, current)
            distSum[current] += distSum[child] + (weight * subTree[child])
            subTree[current] += subTree[child]

def dfs2(current, parent):
    for child, weight in graph[current]:
        if child != parent:
            distSum[child] = distSum[current] + (N - subTree[child] * 2) * weight
            dfs2(child, current)


N = int(input())

subTree = [1] * (N + 1)
distSum = [0] * (N + 1)
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    start, end, weight = map(int, input().split())
    graph[start].append([end, weight])
    graph[end].append([start, weight])


dfs1(1, 1)
dfs2(1, 1)

for num in distSum[1:]:
    print(num)