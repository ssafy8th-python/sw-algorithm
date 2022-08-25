# 노드의 거리
'''
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
1 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9


1
6 4
1 4
1 3
2 3
2 5
1 6
'''

def BFS(s, start, end, N):
    visited = [0] * (N+1)
    q = []
    q.append(start)
    visited[start] = 1
    while q:
        t = q.pop(0)
        for i in s[t]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[t] + 1
                if i == end:
                    return visited[end] -1

    return 0

T = int(input())
for tc in range(1, 1+T):
    N, E = map(int, input().split())
    s = [[] for _ in range(N+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        s[a].append(b)
        s[b].append(a)
    start, end = map(int, input().split())
    print(f'#{tc} ', end='')
    print(BFS(s, start, end, N))
