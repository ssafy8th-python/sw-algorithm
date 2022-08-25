# 2563 색종이
# 주소: https://www.acmicpc.net/problem/2563

# 제출한 답
import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
board = [[0] * 101 for _ in range(101)]

cnt = 0
for square in lst:
    for r in range(square[1], square[1] + 10):
        for c in range(square[0], square[0] + 10):
            if board[r][c] == 0:
                cnt += 1
                board[r][c] = 1

print(cnt)


# 다른 답
N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
lst = [[0]*100 for _ in range(100)]
for i in range(len(a)):
    for j in range(10):
        for k in range(10):
            lst[a[i][0]+j][a[i][1]+k] = 1   # 굳이 체크하지 않고 그냥 전부 1로 만들어버림
ans = 0
for i in range(100):
    ans += sum(lst[i])
print(ans)