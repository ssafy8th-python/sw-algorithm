import sys

while True:
    stack = []
    sentence = sys.stdin.readline().rstrip()
    if sentence == '.':
        break
    result = True
    for i in sentence:
        if i == '(' or i == '[':
            stack.append(i)

        elif i == ')' or i == ']':
            if not stack:
                result = False
                break
            elif i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            else:
                result = False
                break

    if result and not stack:
        print('yes')
    else:
        print('no')




