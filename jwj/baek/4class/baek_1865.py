
INF = int(1e9)


def bellman_ford(start):
    distance = [INF] * (N + 1)
    distance[start] = 0

    for i in range(N):
        for s, e, w in edges:
            # distance[s] != INF 를 지워주었음
            # 그 이유는 start 부분부터 최단거리를 구하는 문제가 아니고 음수 사이클의 존재 유무를 확인하는 문제이기 때문
            if distance[e] > distance[s] + w:
                if i == N - 1:
                    return 1
                distance[e] = distance[s] + w

    return 0


test_case = int(input())

for tc in range(test_case):
    N, M, W = map(int, input().split())

    edges = []

    # 도로는 방향이 없음
    for _ in range(M):
        s, e, w = map(int, input().split())
        edges.append((s, e, w))
        edges.append((e, s, w))

    for _ in range(W):
        s, e, w = map(int, input().split())
        edges.append((s, e, -w))

    res = bellman_ford(1)

    if res:
        print('YES')
    else:
        print('NO')

