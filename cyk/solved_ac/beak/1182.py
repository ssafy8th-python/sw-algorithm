# 부분 수열의 합
# N개의 정수로 이루어진 수열이 있을 때 크기가 양수인 부분수열에서 다 더한 값이 S가 되는 경우의 수

def comb():
    cnt = 0
    for i in range(1<<N):
        tmp = []
        for j in range(N):
            if i & (1<<j):
                tmp.append(lst[j])
        if len(tmp) and sum(tmp) == S:
            cnt += 1
    print(cnt)

N, S = map(int, input().split())
lst = list(map(int, input().split()))
comb()

#
# def solve(k, Sum):
#     global n, s, cnt
#     if k == n:
#         if s == Sum:
#             cnt += 1
#         return
#     solve(k + 1, Sum)
#     solve(k + 1, Sum + nums[k])
