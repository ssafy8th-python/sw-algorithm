# 15663 N과 M(9)
# 주소: https://www.acmicpc.net/problem/15663

# 제출한 답
import sys
input = sys.stdin.readline


def per(cnt):
    if cnt == m:
        results.add(tuple(check))
    else:
        for i in range(n):
            if not used[i]:
                used[i] = 1
                check[cnt] = lst[i]
                per(cnt + 1)
                used[i] = 0
                check[cnt] = 0


n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
results = set()
used = [0] * n
check = [0] * m
per(0)
results = list(results)
results.sort()
for i in results:
    print(*i)


# 다른 답
from sys import stdin

n, m = map(int, stdin.readline().split())
arr = sorted(list(map(int, stdin.readline().split())))
visited = [False] * n
tmp = []

def dfs():
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))
        return
    chk = 0
    for i in range(n):
        if not visited[i] and chk != arr[i]:
            visited[i] = True
            tmp.append(arr[i])
            chk = arr[i]
            dfs()
            visited[i] = False
            tmp.pop()
dfs()