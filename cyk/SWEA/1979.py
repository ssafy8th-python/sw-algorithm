import sys
sys.stdin = open("input (3).txt", "r")
'''
5 3
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1
'''
T = int(input())

def check(arr):
    cnt = 0
    for lst in arr:
        test = []
        for i in range(N):
            if lst[i] == 1:
                test.append(1)
            elif lst[i] == 0:
                if sum(test) == K:
                    cnt += 1
                test = []
        if sum(test) == K:
            cnt += 1
    return cnt

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ver_arr = list(zip(*arr))
    print(f'#{tc} {check(arr)+check(ver_arr)}')

