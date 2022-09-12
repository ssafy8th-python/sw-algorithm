import heapq

test_case = 0
INF = int(1e9)

def dijkstra(x, y):
    q = []

    distance[x][y+1] = distance[x][y] + cave[x][y+1]
    distance[x+1][y] = distance[x][y] + cave[x+1][y]

    heapq.heappush(q, (distance[x][y+1], x, y+1))
    heapq.heappush(q, (distance[x+1][y], x+1, y))

    while q:
        dist, i, j = heapq.heappop(q)

        visited[i][j] = True

        for d_x, d_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n_x = i + d_x
            n_y = j + d_y

            if 0 <= n_x < N and 0 <= n_y < N and not visited[n_x][n_y]:
                new_dist = dist + cave[n_x][n_y]

                if distance[n_x][n_y] > new_dist:
                    distance[n_x][n_y] = new_dist
                    heapq.heappush(q, (new_dist, n_x, n_y))

    return distance[-1][-1]


while True:
    test_case += 1

    N = int(input())

    if N == 0:
        break

    cave = [list(map(int, input().split())) for _ in range(N)]

    distance = [[INF] * N for _ in range(N)]

    visited = [[False] * N for _ in range(N)]

    visited[0][0] = True
    distance[0][0] = cave[0][0]

    print(f"Problem {test_case}: {dijkstra(0, 0)}")
