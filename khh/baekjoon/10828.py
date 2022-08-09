# 첫째 줄 N, 둘째 줄부터 명령이 하나씩
# push X: 정수 X를 스택에 넣는 연산
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력
# size: 스택에 들어있는 정수의 개수를 출력
# empty: 스택이 비어있으면 1, 아니면 0을 출력
# top: 스택의 가장 위에 있는 정수를 출력, 정수가 없는 경우에는 -1을 출력

import sys
n = int(sys.stdin.readline())

stack=[]
for i in range(n):
    order = sys.stdin.readline().split()

    if order[0]=='push':
        stack.append(order[1])
    elif order[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])


# # 입출력 속도 비교 : sys.stdin.readline > raw_input() > input()
# # 반복문으로 여러줄을 입력 받아야 할 때 input()으로 입력 받는다면 시간초과가 발생할 수 있음.
# 한 개의 정수를 입력받을 때 개행문자를 제거 필요
# a = int(sys.stdin.readline())
# https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline