# 1218 괄호 짝짓기
# 주소: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14eWb6AAkCFAYD

import sys
sys.stdin = open("input.txt", "r")

T = 10

for test_case in range(1, T + 1):
    n = int(input())
    word = input()

    stack = []
    flag = True

    open_it = '([{<'
    close_it = ')]}>'

    for i in word:
        if i in open_it:
            stack.append(i)
        else:
            if len(stack) != 0 and close_it.index(i) == open_it.find(stack[-1]):
                stack.pop()
            else:
                flag = False
                break

    if flag and len(stack) == 0:
        result = 1
    else:
        result = 0

    print(f'#{test_case} {result}')
