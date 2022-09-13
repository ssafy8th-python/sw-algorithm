'''
input

3 3
1 2 3
2 3 4
3 1 -8

'''

INF = int(1e9)


def bellman_ford(start):
    distance = [INF] * (V + 1)
    distance[start] = 0

    # 한번더 반복하여 값의 변화 유무에 따라 음수 싸이클인지 확인
    for i in range(V):
        for s, e, w in edges:
            if distance[s] != INF and distance[e] > distance[s] + w:
                if i == V - 1:
                    return distance

                distance[e] = distance[s] + w

    return distance


V, E = map(int, input().split())     # N = node, M = edge

edges= []

for _ in range(E):
    s, e, w = map(int, input().split())
    edges.append((s, e, w))

res = bellman_ford(1)
print(res)

# [1000000000, -2, 2, 6]