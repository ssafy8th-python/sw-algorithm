# n과 m (3)
# 1부터 n까지 자연수 중에서 m개를 고른 수열
# 같은 수를 여러 번 골라도 된다
def repPer(k):
    if k == m:
        print(*result)
        return
    for i in range(1, 1+n):
        result[k] = i
        repPer(k+1)


n, m = map(int, input().split())
result = [-1]*m
repPer(0)