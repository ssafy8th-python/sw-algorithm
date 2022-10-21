# 9019 DSLR
# 주소: https://www.acmicpc.net/problem/9019

# 제출한 답
import sys
from collections import deque
input = sys.stdin.readline


def S(num):
    if num == 0:
        return 9999
    else:
        return num - 1


def L(num):
    tmp1 = num // 1000
    tmp2 = num % 1000
    return tmp2 * 10 + tmp1


def R(num):
    tmp1 = num // 10
    tmp2 = num % 10
    return tmp2 * 1000 + tmp1


def DSLR(num, curC):
    q = deque()
    q.append((num, curC))
    visited[num] = 1
    while q:
        n, s = q.popleft()
        if n == B:
            return s
        De, Su, Le, Ri = (n * 2) % 10000, S(n), L(n), R(n)
        if not visited[De]:
            q.append((De, s + 'D'))
            visited[De] = 1
        if not visited[Su]:
            q.append((Su, s + 'S'))
            visited[Su] = 1
        if not visited[Le]:
            q.append((Le, s + 'L'))
            visited[Le] = 1
        if not visited[Ri]:
            q.append((Ri, s + 'R'))
            visited[Ri] = 1


t = int(input())
for _ in range(t):
    A, B = map(int, input().split())
    visited = [0] * 10000
    print(DSLR(A, ''))
