# 11725 트리의 부모 찾기
# 주소: https://www.acmicpc.net/problem/11725

# 제출한 답1 => 메모리 초과 100,000 * 100,000
# import sys
# input = sys.stdin.readline

# N = int(input())
# graph = [[0] * (N + 1) for _ in range(N + 1)]
# for _ in range(N - 1):
#     nodeA, nodeB = map(int, input().split())
#     graph[nodeA][nodeB] = 1
#     graph[nodeB][nodeA] = 1
#
# results = [0] * (N + 1)
# for r in range(1, N + 1):
#     for c in range(1, N + 1):
#         if graph[r][c] and not results[c] and results[r] != c:
#             results[c] = r
#
# for result in results[2:]:
#     print(result)

# 제출한 답2
# 1부터 bfs나 dfs로 돌면서 다 확인이 낫겟다
import sys
input = sys.stdin.readline

N = int(input())
nodes = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    nodeA, nodeB = map(int, input().split())
    nodes[nodeA].append(nodeB)
    nodes[nodeB].append(nodeA)

results = [0] * (N + 1)
s = [1]
while s:
    v = s.pop()
    for w in nodes[v]:
        if not results[w]:
            results[w] = v
            s.append(w)

for result in results[2:]:
    print(result)
