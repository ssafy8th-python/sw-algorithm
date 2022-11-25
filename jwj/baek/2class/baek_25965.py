N = int(input())

for _ in range(N):
    M = int(input())
    K = []
    D = []
    A = []
    result = 0
    for _ in range(M):
        a, b, c = map(int, input().split())
        K.append(a)
        D.append(b)
        A.append(c)

    k, d, a = map(int, input().split())

    for i in range(M):
        tmp = K[i] * k - D[i] * d + A[i] * a

        if tmp > 0:
            result += tmp

    print(result)