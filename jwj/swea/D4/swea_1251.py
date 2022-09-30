T = int(input())

INF = 10000000


def prim():
    U = [False] * N
    D = [INF] * N
    D[0] = 0

    for _ in range(N):
        minV = INF
        for i in range(N):
            if U[i]:
                continue
            if minV > D[i]:
                minV = D[i]
                curV = i

        U[curV] = True

        for i in range(N):
            if U[i]:
                continue
            n_value = (abs(arr1[curV] - arr1[i]) ** 2 + abs(arr2[curV] - arr2[i]) ** 2) ** 0.5

            if D[i] > n_value:
                D[i] = n_value

    result = 0

    for num in D:
        result += (num * num) * E

    return result


for test_case in range(1, T+1):
    N = int(input())

    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    E = float(input())

    print(f'#{test_case} {round(prim())}')