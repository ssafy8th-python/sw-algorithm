def su(arr):
    maxV = 0
    cnt_up = 1
    cnt_down = 1
    if len(arr) == 1:                    # x같은 반례 1
        return 1

    for i in range(1, n):
        if arr[i-1] <= arr[i]:
            cnt_up += 1
            if cnt_up > maxV:
                maxV = cnt_up
        else:
            cnt_up = 1

        if arr[i-1] >= arr[i]:
            cnt_down += 1
            if cnt_down > maxV:
                maxV = cnt_down
        else:
            cnt_down = 1
    return maxV

n = int(input())
arr = list(map(int, input().split()))

print(su(arr))


# 다른 사람 dp로 푼거
# arr = list(map(int, input().split()))
# dp1, dp2 = [1]*n, [1]*n
# for i in range(1, n):
#     if arr[i] <= arr[i-1]:
#         dp1[i] = max(dp1[i], dp1[i-1]+1)
#     if arr[i] >= arr[i-1]:
#         dp2[i] = max(dp2[i], dp2[i-1]+1)
# print(max(max(dp1), max(dp2)))