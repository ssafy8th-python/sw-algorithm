# import sys

# 시간 초과 코드
# K, N = map(int, sys.stdin.readline().split())
# long = [int(sys.stdin.readline()) for _ in range(K)]
#
# average = sum(long) // N
# cnt = 0
# while cnt != N:
#     for i in long:
#         cnt += i // average
#     if cnt == N:
#         break
#     average -= 1
#     cnt = 0
#
# print(average)

K,N = map(int,input().split())
lst = [int(input()) for _ in range(K)]
start = 1
end = int(sum(lst)/N)

while start <= end :
    middle = (start+end) // 2
    tmp = 0
    for k in lst :
        tmp += k//middle
    if tmp >= N :
        start = middle + 1
    else :
        end = middle -1
print(middle)
