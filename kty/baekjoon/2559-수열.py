import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# 첫 번째 연속된 값의 합을 구하고
# 다음 연속된 값의 합
# = 바로 이전 연속된 온도의 합 - 이전 연속 된 날짜 중 바로 앞 날짜(전날)의 온도 + 다음 연속된 값 에서의 m번째 온도

lst = []
sumV = sum(arr[:m])
lst.append(sumV)
for i in range(1, len(arr)-m+1):
    sumV = sumV-arr[i-1]+arr[i+m-1]
    lst.append(sumV)
print(max(lst))

# 시간초과
# maxV = 0
# for i in range(0, len(arr)-m):
#     cnt = 0
#     for j in range(i, i + m):
#         cnt += arr[j]
#     if cnt > maxV:
#         maxV = cnt
#
# print(maxV)
