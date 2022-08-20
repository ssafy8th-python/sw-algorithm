# Flatten
# 제한된 작업 횟수동안 평탄화 작업을 한 후 최고점과 최저점의 차이를 반환
import sys
sys.stdin = open("input (4).txt", "r")
for tc in range(1, 11):
    N = int(input())
    s = list(map(int, input().split()))
    box_lst = [0] * 101
    for elem in s:
        box_lst[elem] += 1
    mx = max(s)
    mn = min(s)
    while N > 0 :
        box_lst[mx] -= 1
        box_lst[mx-1] += 1
        box_lst[mn + 1] += 1
        box_lst[mn] -= 1
        if box_lst[mx] == 0:
            mx -= 1
        if box_lst[mn] == 0:
            mn += 1
        N -= 1
        res = mx - mn
        if res < 2:
            break
    print(f'#{tc} {res}')

