nam = 1000000007


def virus(inc, t):
    if t == 1:
        return inc

    if t % 2 == 0:
        return virus(inc, t // 2) ** 2 % nam
    else:
        return virus(inc, t // 2) ** 2 * inc % nam


K, P, N = map(int, input().split())

result = virus(P, N)

print(K * result % nam)

