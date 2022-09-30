# 창용 마을 무리의 개수
import sys
sys.stdin = open("s_input.txt", "r")

def find_set(x):
    while x != lst[x]:
        x = lst[x]
    return x
def union(x,y):
    lst[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    lst = [x for x in range(N+1)]
    cnt = 0
    for _ in range(M):
        n1, n2 = map(int, input().split())
        union(n1, n2)

    for i in range(1,N+1):
        if lst[i] == i:
            cnt += 1
    print(f'#{tc} {cnt}')