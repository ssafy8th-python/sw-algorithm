isp = {'(' : 0, '+' : 1, '*' : 2}
icp = {'(' : 3, '+' : 1, '*' : 2}


def step1():
    for char in strs:
        if '1' <= char <= '9':
            postfix.append(char)

        elif char ==')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()

        elif not stack or isp[stack[-1]] < icp[char]:
            stack.append(char)

        elif isp[stack[-1]] >= icp[char]:
            while stack and isp[stack[-1]] >= icp[char]:
                postfix.append(stack.pop())
            stack.append(char)

    while stack:
        postfix.append(stack.pop())


def step2():
    for char in postfix:
        if '1' <= char <= '9':
            stack.append(int(char))
        elif char == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(b+a)
        elif char == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(b*a)


for tc in range(1, 11):
    N = int(input())
    strs = list(input())
    stack = []
    postfix = []
    step1()
    step2()

    print(f'#{tc} {stack[-1]}')
