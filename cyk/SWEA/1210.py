# 사다리타기
# 지정된 도착점에 대응되는 출발점 x를 반환하는 코드를 작성하라
import sys
sys.stdin = open("input (4).txt", "r")
for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)] # 100 x 100
    goal_idx = 0
    for i in range(0,100):
        if ladder[99][i] == 2:
            goal_idx = i            # case1: 57, 목표지점의 index
            break
    row = 99
    while row > 0:
        if goal_idx - 1 >= 0 and ladder[row][goal_idx-1] == 1:
            goal_idx -= 1
        elif goal_idx +1 < 100 and ladder[row][goal_idx +1] == 1:
            goal_idx += 1
        else:
            row -= 1
        ladder[row][goal_idx] = 0

    print(f'#{tc} {goal_idx}')