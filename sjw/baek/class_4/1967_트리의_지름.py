# 1967 트리의 지름
# 주소: https://www.acmicpc.net/problem/1967

# 제출한 답
import sys
input = sys.stdin.readline


def dfs(start):
    visited = [0] * (n + 1)
    stack = [[start, 0]]
    visited[start] = 1

    node, distance = start, 0
    while stack:
        cNode, cDistance = stack.pop()
        if cDistance > distance:
            distance = cDistance
            node = cNode

        if parents[cNode]:
            p, w = parents[cNode]
            if not visited[p]:
                visited[p] = 1
                stack.append([p, cDistance + w])
        for c, w in children[cNode]:
            if not visited[c]:
                visited[c] = 1
                stack.append([c, cDistance + w])

    return [node, distance]


n = int(input())
parents = [0] * (n + 1)
children = [[]for _ in range(n + 1)]

for _ in range(n - 1):
    p, c, w = map(int, input().split())
    children[p].append([c, w])
    parents[c] = [p, w]

node1, tmp = dfs(1)
node2, answer = dfs(node1)

print(answer)


# 다른 답1  508ms

from collections import defaultdict, deque

n = int(input())
graph = defaultdict(dict)

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c


dist = [-1 for _ in range(n+1)]
def bfs(start):
    dist[start] = 0
    que = deque([(start, 0)])
    while que:
        i, d = que.popleft()
        for a in graph[i]:
            if dist[a] == -1:
                new_d = d + graph[i][a]
                dist[a] = new_d
                que.append((a, new_d))

bfs(1)
far = max([i for i in range(1, n+1)], key=lambda x: dist[x])

for i in range(n+1):
    dist[i] = -1
bfs(far)

print(max(dist))
