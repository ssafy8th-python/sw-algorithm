

N = int(input())

arr = list(map(int, input().split()))

# 정방향
dp1 = [1] * N
for i in range(1, N):
    for j in range(0, i):
        if arr[i] > arr[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)


# 거꾸로 LIS
dp2 = [1] * N
for i in range(N-2, -1, -1):
    for j in range(N-1, i-1, -1):
        if arr[i] > arr[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

maxV = 0

# 합의 값이 가장 클 때 가장 긴 바이토닉 부분수열이 완성됨
for i in range(N):
    tmp = dp1[i] + dp2[i]

    if maxV < tmp:
        maxV = tmp

print(maxV - 1)