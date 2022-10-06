

def mul(U, V):
    Z = [[0] * N for _ in range(N)]

    for row in range(N):
        for col in range(N):
            e = 0
            for i in range(N):
                e += U[row][i] * V[i][col]
            Z[row][col] = e % 1000

    return Z


def square(n):
    if n == 1:
        return M

    tmp = square(n//2)

    if n % 2:
        return mul(mul(tmp, tmp), M)
    else:
        return mul(tmp, tmp)


N, B = map(int, input().split())

M = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        M[i][j] %= 1000

result = square(B)

for r in result:
    print(*r)