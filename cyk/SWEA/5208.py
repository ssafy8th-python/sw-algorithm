# 전기버스2
# 목적지에 도착하는데 필요한 최소한의 교환횟수
'''
3
5 2 3 1 1
10 2 1 3 2 2 5 4 2 1
10 1 1 2 1 2 2 1 2 1
'''

def charge(k, remain, cnt):
    global mn
    if k == N-1:
        if mn > cnt:
            mn = cnt
        return
    if mn <= cnt:
        return
    if remain == 0:
        return

    charge(k+1, remain-1, cnt)
    charge(k+1, lst[k+1], cnt+1)


T = int(input())
for tc in range(1, 1+T):
    lst = list(map(int, input().split()))
    N, lst = lst[0], lst[1:]+[0]
    mn = N
    charge(0,lst[0], 0)
    print(f'#{tc} {mn}')