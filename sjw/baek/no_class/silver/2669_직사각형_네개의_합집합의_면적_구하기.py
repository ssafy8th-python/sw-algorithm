# 2669 직사각형 네개의 합집합의 면적 구하기
# 주소: https://www.acmicpc.net/problem/2669

# 제출한 답
import sys
input = sys.stdin.readline

lst = [list(map(int, input().split())) for _ in range(4)]
board = [[0] * 101 for _ in range(101)]

cnt = 0
for square in lst:
    for r in range(square[1], square[3]):
        for c in range(square[0], square[2]):
            if board[r][c] == 0:
                cnt += 1
                board[r][c] = 1

print(cnt)


# 다른 답
box = [[0] * 100 for _ in range(100)]
for TC in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):      # +1을 하나 안하나 어차피 계산되는 넓이는 같음
        for j in range(x1, x2):  # 굳이 모양에 집착하지 말아야함
            box[i][j] = 1

count = 0
for i in range(len(box)):
    for j in range(len(box)):
        if box[i][j] > 0:
            count += 1
print(count)