# 전자카트
import sys
sys.stdin = open("sample_input (7).txt", "r")
T = int(input())
def f(k):
    global res
    if k == n:       # n개의 구역 순회 완료
        res.append(result+[0])
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            result[k] = i
            if result[0] == 0:
                f(k+1)
            visited[i] = False


for tc in range(1, 1+T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [False]*n
    result = [-1] *n
    res=[]
    f(0)
    mn = 100000000000
    for idx, lst in enumerate(res):
        tmp=0
        for i in range(len(lst)-1):
            tmp += arr[lst[i]][lst[i+1]]
        if mn > tmp:
            mn = tmp
    print(f'#{tc} {mn}')


# 다른 풀이
T = int(input())

INF = 1000


def dfs(start, status, cnt):
    global result

    if result <= status:
        return

    if cnt == N - 1:
        value = status + arr[start][0]

        if result > value:
            result = value

    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                dfs(i, status + arr[start][i], cnt + 1)
                visited[i] = False


for test_case in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    visited[0] = True
    result = INF

    dfs(0, 0, 0)

    print(f'#{test_case} {result}')