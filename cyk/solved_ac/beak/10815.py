# 숫자카드
# 이진탐색
import sys
input = sys.stdin.readline

def find(key):
    start = 0
    end = N - 1
    while start <= end:
        middle = (start + end) //2
        if lst[middle] == key:
            return 1
        if lst[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return 0

N = int(input())
lst = sorted(list(map(int, input().split())))
M = int(input())
checking = list(map(int, input().split()))

for key in checking:
    print(find(key), end=' ')

