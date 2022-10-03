# N과 M (7)
def H(k):
    if k == M:
        print(*result)
        return
    for i in range(N):
        result[k] = lst[i]
        H(k+1)



N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
result = [-1]* M
H(0)