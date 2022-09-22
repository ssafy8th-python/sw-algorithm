def f(r):
    if r == M:
        print(*lst)
    else:
        for i in range(N):
            lst[r] = i + 1
            f(r+1)
            lst[r] = 0


N, M = map(int, input().split())

lst = [0] * M

f(0)
