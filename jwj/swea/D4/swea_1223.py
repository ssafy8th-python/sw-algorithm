ISP = {'(': 0, '+': 1, '*': 2}


def step1():
    for char in strs:
        if '1' <= char <= '9' or char == '(':
            postIndex.append(char)
        elif not stack:
            stack.append(char)
        elif char == ')':
            while char != '(':
                postIndex.append(stack.pop())
            stack.pop()
        else:
            while stack and ISP[char] <= ISP[stack[-1]]:
                postIndex.append(stack.pop())

            stack.append(char)

    while stack:
        postIndex.append(stack.pop())


def step2():
    for char in postIndex:
        if '1' <= char <= '9':
            stack.append(int(char))
        elif char == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(a*b)


for tc in range(1, 11):
    N = int(input())

    strs = input()

    postIndex = []

    stack = []

    step1()
    step2()

    print(f'#{tc} {stack[-1]}')
