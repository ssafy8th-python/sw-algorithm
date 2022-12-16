import heapq

T = int(input())


def dijkstra(start):
    h = []
    heapq.heappush(h, [0, start])
    d = [int(1e9)] * (n + 1)
    d[start] = 0

    while h:
        weight, node = heapq.heappop(h)

        for v, w in G[node]:
            n_w = weight + w
            if d[v] > n_w:
                d[v] = n_w
                heapq.heappush(h, [n_w, v])

    return d


for _ in range(T):
    n, m, t = map(int, input().split())
    G = [[] for _ in range(n + 1)]
    destination = []

    s, g, h = map(int, input().split())

    for _ in range(m):
        a, b, d = map(int, input().split())

        G[a].append([b, d])
        G[b].append([a, d])

    for _ in range(t):
        destination.append(int(input()))

    start_d = dijkstra(s)
    g_d = dijkstra(g)
    h_d = dijkstra(h)

    res = []
    for dest in destination:
        if start_d[dest] == start_d[g] + g_d[h] + h_d[dest]:
            res.append(dest)
        elif start_d[dest] == start_d[h] + h_d[g] + g_d[dest]:
            res.append(dest)

    res.sort()

    print(*res)
