import sys; input = sys.stdin.readline

def dfs(r, c, idx, total):
    global ans

    # 이미 계산한 total 값에 여러개의 max_val을 더한 결과보다 ans가 크다면
    # 해당 값이 가질 수 있는 최대값 보다 크거나 같은 값을 이미 ans가 갖고 있기 때문에 
    # 다음 값을 계산하지 않고 return 합니다.
    if ans >= total + max_val * (3 - idx):
        return

    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                
                if idx == 1:    
                    visit[nr][nc] = 1
                    dfs(r, c, idx + 1, total + arr[nr][nc]) # 위치는 이동하지 않고 다른 부분 값 더하기  그 이유는 ㅗ 자형을 만들기 위해 갔다가 돌아와야 하기 때문
                    visit[nr][nc] = 0
                visit[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + arr[nr][nc])   # 위치를 이동해서 다른 모양을 만들기 위해
                visit[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0
max_val = max(map(max, arr))

for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        visit[r][c] = 0

print(ans)