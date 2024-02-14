# 28431 양말 짝 맞추기
# 주소: https://www.acmicpc.net/problem/28431

# 제출한 답
# import sys
# input = sys.stdin.readline

count = [0] * 10
for _ in range(5):
    num = int(input())
    count[num] += 1

answer = 0
for i in range(10):
    if count[i] % 2:
        answer = i

print(answer)
