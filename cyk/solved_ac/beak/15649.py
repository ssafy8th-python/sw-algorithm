# n과 m(1)
# 1부터 n까지 자연수 중에서 중복 없이 m개를 고른 수열
def per(k):
    if k == m:
        print(*result)
        return

    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True
            result[k] = i
            per(k+1)
            visited[i] = False
n, m = map(int, input().split())

visited = [False]*(n+1)
result = [-1]*m
per(0)
