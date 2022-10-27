# 15657 N과 M(8)
# 주소: https://www.acmicpc.net/problem/15657

# 제출한 답
import sys
input = sys.stdin.readline

def func(s, c):
    if c == m:
        result = []
        for i in range(n):
            if arr[i]:
                for _ in range(arr[i]):
                    result.append(lst[i])
        print(*result)
    else:
        for i in range(s, n):
            arr[i] += 1
            func(i, c + 1)
            arr[i] -= 1


n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
arr = [0] * n
func(0, 0)