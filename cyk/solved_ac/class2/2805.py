# 나무자르기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())    # 나무의 개수,
tree = list(map(int, input().split()))
start, end = 1, max(tree)

while start <= end:
    sum = 0
    middle = (start+end)//2
    for elem in tree:
        if elem > middle:
            sum += (elem - middle)

    if sum >= M:
        start = middle + 1
    else:
        end = middle - 1
print(end)