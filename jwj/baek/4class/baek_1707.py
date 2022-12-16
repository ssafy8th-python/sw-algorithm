from collections import deque
import sys
input = sys.stdin.readline

r_g = {'r': 'b', 'b': 'r'}

K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    vertex_color = [0] * (V + 1)

    q = deque()

    result = 'YES'
    for index in range(1, V+1):
        if not G[index]:
            vertex_color[index] = 1
            continue
        elif vertex_color[index]:
            continue

        vertex_color[index] = 'r'
        q.append(index)

        while q:
            cur_index = q.popleft()
            next_color = r_g[vertex_color[cur_index]]

            next_G = G[cur_index]

            for next_index in next_G:
                # next_index 값이 0일 때 q에 넣고 color 변경해주기
                if vertex_color[next_index] == 0:
                    vertex_color[next_index] = next_color
                    q.append(next_index)
                elif vertex_color[next_index] == r_g[next_color]:
                    result = 'NO'
                    break

            if result == 'NO':
                break

        if result == 'NO':
            break

    print(result)

