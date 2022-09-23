# 최적경로
import sys
sys.stdin = open("input (12).txt", "r")

def perm(pos, depth, dist):
    global mn
    if dist >= mn:
        return

    if depth == n:
        if mn > dist+abs(ipt[pos*2]-ipt[2]) + abs(ipt[pos*2+1]-ipt[3]):
            mn = dist+abs(ipt[pos*2]-ipt[2]) + abs(ipt[pos*2+1]-ipt[3])
        return

    for i in range(2, n+2):
        if not visited[i]:
            visited[i] = True
            perm(i, depth+1, dist + abs(ipt[pos*2]-ipt[i*2]) + abs(ipt[pos*2+1]-ipt[i*2+1]))
            visited[i] = False

T = int(input())

for tc in range(1, 1+T):
    n = int(input())
    ipt = list(map(int, input().split()))
    visited = [False]*(n+2)
    visited[0] = True
    visited[1] = True
    mn = 10000
    perm(0, 0, 0)
    print(f'#{tc} {mn}')