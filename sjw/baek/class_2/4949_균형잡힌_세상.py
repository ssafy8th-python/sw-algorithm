# 4949 균형잡힌 세상
# 주소: https://www.acmicpc.net/problem/4949

# So when I die (the [first] I will see in (heaven) is a score list).
# [ first in ] ( first out ).
# Half Moon tonight (At least it is better than no Moon at all].
# A rope may form )( a trail in a maze.
# Help( I[m being held prisoner in a fortune cookie factory)].
# ([ (([( [ ] ) ( ) (( ))] )) ]).
#  .
# .
import sys
input = sys.stdin.readline      # 빠른 입력


while True:                     # .이 나오기 전까지 계속 반복
    word = []                   # stack
    flag = True                 # yes, no 판별
    balanced_world = input().rstrip()   # rstrip(): 개행문자 /n 제거

    if balanced_world == '.':           # while 탈출
        break

    for i in balanced_world:
        if i == '[' or i == '(':        # 왼쪽 괄호면 top에 추가
            word.append(i)
        elif i == ']' or i == ')':      # 오른쪽 괄호일 때
            if len(word) == 0:          # 스택이 비어있다면
                flag = False            # no
                break                   # for 탈출
            elif i == ']' and word[-1] == '[' or i == ')' and word[-1] == '(':  # peek과 i가 짝이라면
                word.pop()              # 스택 pop
            else:                       # 짝이 안맞다면
                flag = False            # no
                break                   # for 탈출

    if flag and len(word) == 0:         # flag가 True이고 스택이 비어있다면
        print('yes')                    # yes 출력
    else:                               # 아니라면
        print('no')                     # no 출력
