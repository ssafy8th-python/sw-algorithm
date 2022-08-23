T = int(input())


def step2():
    for char in postfix:
        if '1' <= char <= '9':
            stack.append(int(char))
        elif len(stack) >= 2:
            if char == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(b+a)
            elif char == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(b*a)
            elif char == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(b//a)
            elif char == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append((b-a))
        elif len(stack) < 2:
            if char != '.':
                return 0
            else:
                return 1


for tc in range(1, T+1):
    stack = []
    postfix = list(input().split())
    res = step2()

    if res:
        print(f'#{tc} {stack[-1]}')
    else:
        print(f'#{tc} error')
