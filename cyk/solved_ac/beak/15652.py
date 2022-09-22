# n과 m (4)

def per(k, s):
    if k == M:
        print(*result)
        return

    for i in range(s, N):
        result[k] = i+1
        per(k+1, i)

N, M = map(int, input().split())
result = [-1]*M
per(0, 0)