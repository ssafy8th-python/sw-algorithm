def f(r):
    if r == M:
        for i in range(M):
            if p[i]:
                print(p[i], end=" ")
        print()
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                p[r] = i+1
                f(r+1)
                visited[i] = False


N, M = map(int, input().split())

p = [0 for _ in range(N)]

visited = [False] * N

f(0)

