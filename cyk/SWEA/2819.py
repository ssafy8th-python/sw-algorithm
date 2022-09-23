# 격자판의 숫자 이어붙이기
def dfs(r, c, number,cnt):
    global res
    if cnt == 7:
        # print(number)
        if not number in res:
            res.append(number)
        return
    st = [(r,c)]

    while st:
        cR, cC = st.pop()
        for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]]:
            nr, nc = cR + dr, cC + dc
            if 0 <= nr < 4 and 0 <= nc < 4:
                dfs(nr, nc, number+str(arr[nr][nc]), cnt+1)

T = int(input())
for tc in range(1, 1+T):
    arr = [list(map(int, input().split())) for _ in range(4)]
    res = []
    number = ''
    for i in range(4):
        for j in range(4):
            dfs(i,j,number,0)
    print(f'#{tc} {len(res)}')