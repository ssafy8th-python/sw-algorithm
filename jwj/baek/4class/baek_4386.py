INF = 100000


def prim():
    U = [False] * N
    D = [INF] * N
    D[0] = 0

    for _ in range(N):
        minV = INF

        for i in range(N):
            if U[i]: continue
            if minV > D[i]:
                minV = D[i]
                curV = i

        U[curV] = True

        for i in range(N):
            if U[i]: continue
            n_v = (abs(x_arr[curV] - x_arr[i]) ** 2 + abs(y_arr[curV] - y_arr[i]) ** 2) ** 0.5

            if D[i] > n_v:
                D[i] = n_v
    return sum(D)


N = int(input())

x_arr = []
y_arr = []

for _ in range(N):
    n1, n2 = map(float, input().split())

    x_arr.append(n1)
    y_arr.append(n2)

print(round(prim(), 2))
