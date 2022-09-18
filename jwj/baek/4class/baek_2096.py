import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

min_ans = [arr[0], arr[1], arr[2]]
max_ans = [arr[0], arr[1], arr[2]]

for arr in range(1, N):
    a, b, c = map(int, input().split())

    min0 = min(min_ans[0], min_ans[1])
    max0 = max(max_ans[0], max_ans[1])

    min1 = min(min_ans[2], min(min_ans[0], min_ans[1]))
    max1 = max(max_ans[2], max(max_ans[0], max_ans[1]))

    min2 = min(min_ans[2], min_ans[1])
    max2 = max(max_ans[2], max_ans[1])

    min_ans[0] = a + min0
    max_ans[0] = a + max0

    min_ans[1] = b + min1
    max_ans[1] = b + max1

    min_ans[2] = c + min2
    max_ans[2] = c + max2


print(max(max_ans), min(min_ans))