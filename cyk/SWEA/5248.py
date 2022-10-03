# 그룹 나누기
import sys
sys.stdin = open("sample_input (4).txt", "r")

def find_set(x):
    while x != lst[x]:
        x = lst[x]
    return x
def union(x, y):
    lst[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, 1+T):
    cnt = 0
    N, M = map(int, input().split())
    ipt = list(map(int, input().split()))
    lst = [0]*(N+1)
    for i in range(1, N+1):
        lst[i] = i
    for i in range(M):
        union(ipt[i*2],ipt[i*2+1])

    for i in range(1, N+1):
        if i == lst[i]:
            cnt += 1

    print(f'#{tc} {cnt}')
