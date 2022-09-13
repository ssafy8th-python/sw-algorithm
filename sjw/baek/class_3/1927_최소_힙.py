# 1927 최소 힙
# 주소: https://www.acmicpc.net/problem/1927

# 제출한 답
import sys
input = sys.stdin.readline


def hitit(k):
    global last
    last += 1
    arr[last] = k
    p = last // 2
    c = last
    while p and arr[p] > arr[c]:
        arr[p], arr[c] = arr[c], arr[p]
        c = p
        p = p // 2


def getit(k):
    global last
    if last <= 0:
        return 0

    tmp = arr[1]
    arr[1] = arr[last]
    last -= 1

    p = 1
    c = 2
    while c <= last:
        if c + 1 <= last and arr[c] > arr[c + 1]:
            c += 1
        if arr[p] > arr[c]:
            arr[p], arr[c] = arr[c], arr[p]
            p = c
            c = p * 2
        else:
            break

    return tmp


n = int(input())

arr = [0] * (n + 1)
last = 0
for _ in range(n):
    a = int(input())
    if a:
        hitit(a)
    else:
        print(getit(1))
