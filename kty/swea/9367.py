import sys

sys.stdin = open("input_9367.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    maxC = 0
    cnt = 1
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]-1:
            cnt += 1
        else:
            if maxC < cnt:
                maxC = cnt
            cnt = 1
    if maxC < cnt:
        maxC = cnt

    print(f'#{tc} {maxC}')