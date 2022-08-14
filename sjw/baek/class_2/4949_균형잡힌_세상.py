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

while True:
    word = []
    flag = True
    balanced_world = input()

    if balanced_world == '.':
        break

    for i in balanced_world:
        if i == '[' or i == '(':
            word.append(i)
        elif i == ']' or i == ')':
            if len(word) == 0:
                flag = False
                break
            elif i == ']' and word[-1] == '[':
                word.pop()
            elif i == ')' and word[-1] == '(':
                word.pop()
            else:
                flag = False
                break
    if flag and len(word) == 0:
        print('yes')
    else:
        print('no')