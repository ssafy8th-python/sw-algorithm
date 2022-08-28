# 2491 수열
# 주소: https://www.acmicpc.net/problem/2491

# 제출한 답
n = int(input())
n_lst = list(map(int, input().split()))

cntP = 1
cntM = 1
maxV = 1  # 길이가 1일 때
for i in range(1, n):
    if n_lst[i - 1] <= n_lst[i]:
        cntP += 1
        if maxV <= cntP:
            maxV = cntP
    else:
        cntP = 1
    if n_lst[i - 1] >= n_lst[i]:
        cntM += 1
        if maxV <= cntM:
            maxV = cntM
    else:
        cntM = 1

print(maxV)
