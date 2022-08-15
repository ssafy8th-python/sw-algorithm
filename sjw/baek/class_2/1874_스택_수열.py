# 1874 스택 수열
# 주소: https://www.acmicpc.net/problem/1874

# 제출한 답
import sys
input = sys.stdin.readline

n = int(input())
stack_lst = [int(input()) for _ in range(n)]
j = 0

stack = []
result = []

for i in range(1, n + 1):
    stack.append(i)
    result.append('+')

    while len(stack) != 0 and stack_lst[j] == stack[-1]:
        stack.pop()
        result.append('-')
        j += 1

if stack:
    print('NO')
else:
    for k in result:
        print(k)