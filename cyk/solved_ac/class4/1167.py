# 트리의 지름
# 임의의 두 점 사이의 거리 중 가장 긴 것
# 트리의 지름을 구성하는 노드는 리프 노드이다
# 1. 아무 점이나 잡고 이 점에서 가장 거리가 먼 점 t를 잡는다.
# 2. t에서 가장 거리가 먼 점 u를 찾는다.
# 3. 트리의 지름은 t-u이다.
import sys
input = sys.stdin.readline

def dfs(k, dist):
    for n, w in tree[k]:
        if visited[n] == -1:
            visited[n] = w + dist
            dfs(n, w+dist)

V = int(input())
tree = [[] for _ in range(V+1)]
for _ in range(V):
    ipt = list(map(int, input().split()))
    s = ipt[0]
    for i in range(1, len(ipt)-1, 2):
        tree[s].append((ipt[i],ipt[i+1]))

visited = [-1]*(V+1)
visited[1] = 0
dfs(1, 0)

t = visited.index(max(visited))

visited = [-1]*(V+1)
visited[t] = 0
dfs(t, 0)
print(max(visited))