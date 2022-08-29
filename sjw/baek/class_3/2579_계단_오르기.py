# 2579 계단 오르기
# 주소: https://www.acmicpc.net/problem/2579

# 점화식
# i번째 계단은 i - 2까지 누적된 값에서 오는 경우와 i - 3까지 누적된 값에 i - 1을 거쳐서 오는 두 가지 경우가 있음

# 제출한 답1
# import sys
# input = sys.stdin.readline

# bottom-up 방식
n = int(input())
n_lst = [int(input()) for _ in range(n)]
n_lst = n_lst + [0] * 300
dp = [n_lst[0], n_lst[0] + n_lst[1], n_lst[2] + max(n_lst[0], n_lst[1])] + [0] * 297


for i in range(3, n):
    dp[i] = n_lst[i] + max(dp[i - 2], dp[i - 3] + n_lst[i - 1])

print(dp[n - 1])


# 제출한 답2
# import sys
# input = sys.stdin.readline

# top-down 방식
def stair(i):
    if i < 0:
        return 0
    elif i == 0:
        return dp[0]
    elif i == 1:
        return dp[1]
    else:
        if dp[i] != 0:  # 저장된 값을 사용하는 과정 memoization 없으면 시간초과가 남
            return dp[i]
        else:
            dp[i] = n_lst[i] + max(stair(i - 2), stair(i - 3) + n_lst[i - 1])
            return dp[i]


n = int(input())
n_lst = [int(input()) for _ in range(n)]
n_lst = n_lst + [0] * 300
dp = [n_lst[0], n_lst[0] + n_lst[1], n_lst[2] + max(n_lst[0], n_lst[1])] + [0] * 297

print(stair(n - 1))
