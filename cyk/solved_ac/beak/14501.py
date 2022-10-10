# 퇴사
def dfs(k, state):
    global mx
    if k > N:
        return
    if k == N:
        if mx < state:
            mx = state
        return
    dfs(k+lst[k][0], state+lst[k][1])
    dfs(k+1, state)

N = int(input())
lst = []
mx = 0
for _ in range(N):
    lst.append(list(map(int, input().split())))
dfs(0, 0)
print(mx)