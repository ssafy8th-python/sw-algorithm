# 배열 최소합
T = int(input())
def per(k, S):
    global result
    if S >= result: # 합이 result 보다 크다면 중지
        return
    if k == n:  # 종료
        if S < result:  # 최소합인지 판별
            result = S
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            per(k+1, S+arr[k][i])
            visited[i] = False

for tc in range(1, 1+T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 100
    visited = [False] * n
    per(0, 0)
    print(f'#{tc} {result}')