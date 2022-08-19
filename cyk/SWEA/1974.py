# 스도쿠 검증
import sys
sys.stdin = open("input (2).txt", "r")

T = int(input())

def test(lst):               # 중복 숫자 테스트 함수
    num_lst = [0] * 10
    for elem in lst:
        num_lst[elem] += 1
        if 2 in num_lst:
            return 0
    return 1

for tc in range(1, 1+T):
    arr = [list(map(int, input().split())) for _ in range(9)]

    res = []

    print(f'#{tc} ', end='')

    for lst in arr:             # 가로 판별
        if test(lst) == 0:
            res.append(0)
            break

    ver_arr = list(zip(*arr))   # 세로 판별
    for lst in ver_arr:
        if test(list(lst)) == 0:
            res.append(0)
            break

    for i in range(0,9,3):      # 격자 판별
        for j in range(0,9,3):
            grid_arr = []
            for k in range(3):
                for t in range(3):
                    grid_arr.append(arr[i+k][i+t])
                    if test(grid_arr) == 0:
                        res.append(0)
                        break
    if 0 in res:
        print(0)
    else:
        print(1)