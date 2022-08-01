import sys

input = sys.stdin.readline

def dfs(init, start):
    global result_lst, N

    if init == start:
        return

    for j in range(N):
        if result_lst[start][j] == 1 and result_lst[init][j] == 0:
            result_lst[init][j] = 1
            dfs(init, j)

N = int(input())

result_lst = [[0] * N for _ in range(N)]

for i in range(N):
    for j, num in enumerate(list(map(int, input().split()))):
        if num == 1:
            result_lst[i][j] = 1


for i in range(N):
    for j in range(N):
        if result_lst[i][j] == 1:
            dfs(i, j)

for i in result_lst:
    for j in i :
        print(j, end=' ')
    print()