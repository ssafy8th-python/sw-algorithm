def perm(r):

    if r == N:
        print(*lst)
        return

    for i in range(N):
        if not used[i]:
            used[i] = True
            lst[r] = i + 1
            perm(r+1)
            used[i] = False


N = int(input())

lst = [i for i in range(1, N+1)]

used = [False] * N
perm(0)
