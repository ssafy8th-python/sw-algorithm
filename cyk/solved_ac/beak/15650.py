# n과 m (2)
# 1부터 n까지 자연수 중에서 중복 없이 m개를 고른 수열
# 고른 수열은 오름차순이어야 한다

def comb(k, s):
    if k == m:
        print(*result)
        return

    for i in range(s, n-(m-k)+1):
        result[k] = i+1
        comb(k+1, i+1)

n, m = map(int, input().split())
result = [-1] * m
comb(0,0)