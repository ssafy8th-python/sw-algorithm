import sys
input = sys.stdin.readline


def binary_search(target):
    start = 0
    end = len(LIS) - 1
    tmp = 0

    while start <= end:
        mid = (start + end) // 2

        if LIS[mid] == target:
            return mid

        if LIS[mid] < target:
            start = mid + 1

        else:
            end = mid - 1
            tmp = mid

    return tmp


N = int(input())

arr = list(map(int, input().split()))

LIS = [arr[0]]

for i in arr[1:]:
    if LIS[-1] < i:
        LIS.append(i)
    else:
        idx = binary_search(i)
        LIS[idx] = i

print(len(LIS))