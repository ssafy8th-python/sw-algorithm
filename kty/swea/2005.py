import sys

sys.stdin = open("input_2005.txt", "r")
                                                                # memoization 풀이
memo = [[1] + [0] * 9 for _ in range(10)]                       # 맨앞은 항상 1이니깐 미리 1 넣어둠
def pas(row, col):
    if memo[row][col] == 0 and row > 0:                         # memo안에 값이 0이면 (없으면), 범위 밖 제한
        memo[row][col] = pas(row-1, col-1) + pas(row-1, col)    # 자신의 왼쪽과 오른쪽 위의 숫자의 합을 넣음
    return memo[row][col]                                       # memo안에 값이 있으면 바로 return

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')
    for row in range(N):
        for col in range(row+1):
            print(pas(row, col), end=' ')
        print()

