# 11723 집합
# 주소: https://www.acmicpc.net/problem/11723

# 제출한 답
import sys
input = sys.stdin.readline

s = [False] * 21

for _ in range(int(input())):
    order = input().rstrip()

    if 'add' in order:
        s[int(order[-1])] = True
    elif 'remove' in order:
        s[int(order[-1])] = False
    elif 'check' in order:
        print(int(s[int(order[-1])]))
    elif 'toggle' in order:
        if s[int(order[-1])]:
            s[int(order[-1])] = False
        else:
            s[int(order[-1])] = True
    elif order == 'all':
        s = [True] * 21
    elif order == 'empty':
        s = [False] * 21
