
'''
input
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4

output
1 2 5 3 6 4 7
'''

from collections import deque

v, e = map(int, input().split())

G = [[] for i in range(v+1)]

in_degree = [0] * (v + 1)

for _ in range(e):
    S, E = map(int, input().split())
    G[S].append(E)

    in_degree[E] += 1

# 1. 진입차수가 0인 노드들을 Queue에 넣기

q = deque()

for i in range(1, v+1):
    if not in_degree[i]:
        q.append(i)

result = []

# q의 값이 비어있을 때 까지 수행
while q:
    now = q.popleft()
    result.append(now)

    # 현재 노드에서 가는 모든 노드 방문
    for i in G[now]:
        in_degree[i] -= 1

        # 전입 차수가 0이면 q에 넣기
        if in_degree[i] == 0:
            q.append(i)


print(result)

