# 연산자 끼워넣기

def dfs(start, status, cnt):
    global mx, mn
    if cnt == n - 1:
        if mx < status:
            mx = status
        if mn > status:
            mn = status
        return

    for i in range(n-1):
        if not visited[i]:
            visited[i] = True
            if opt_lst[i] == 'plus':
                dfs(start+1, (status+n_lst[start]), cnt+1)
                visited[i] = False
            elif opt_lst[i] == 'minus':
                dfs(start+1, (status-n_lst[start]), cnt+1)
                visited[i] = False
            elif opt_lst[i] == 'mult':
                dfs(start+1, (status*n_lst[start]), cnt+1)
                visited[i] = False
            elif opt_lst[i] == 'div':
                dfs(start+1, status//n_lst[start] if status > 0 else -(abs(status)//n_lst[start]), cnt+1)
                visited[i] = False


n = int(input())
n_lst = list(map(int, input().split()))
opt_cnt = list(map(int, input().split()))   # 연산자의 총 개수: n-1
opt_lst = ['plus']*opt_cnt[0] + ['minus']*opt_cnt[1] + ['mult']*opt_cnt[2] + ['div']*opt_cnt[3]

# print(opt_lst)  # ['plus', 'plus', 'minus', 'mult', 'div']
visited = [False]*(n-1)
mx,mn = -10e9, 10e9
dfs(1, n_lst[0], 0)
print(mx)
print(mn)
