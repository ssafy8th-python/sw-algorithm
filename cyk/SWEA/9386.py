import sys
sys.stdin = open("input1.txt", "r")

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    s = list(map(int, input()))
    cnt = 0
    cnt_lst = []
    for i in s:
        if i == 1:
            cnt += 1
            cnt_lst.append(cnt)
        else:
            cnt = 0
    maxV = cnt_lst[0]
    for elem in cnt_lst[1:]:
        if maxV < elem:
            maxV = elem
    print(f'#{tc} {maxV}')