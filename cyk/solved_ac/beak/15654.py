# N과 M(5)
# 길이가 m인 수열을 모두 구하는 프로그램
N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
visited = [False]*N
result = [-1]*M
def comb(k):
    if k == M:
        print(*result)
        return
    for i in range(N):
        if not visited[i]:
            result[k] = lst[i]
            visited[i] = True
            comb(k+1)
            visited[i] = False
comb(0)