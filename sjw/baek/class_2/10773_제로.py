# 10773 제로
# 주소: https://www.acmicpc.net/problem/10773

# 제출한 답
import sys
input = sys.stdin.readline

t = int(input())
stack = []

for i in range(t):
    jung_soo = int(input())

    if jung_soo == 0:
        stack.pop()
    else:
        stack.append(jung_soo)

print(sum(stack))