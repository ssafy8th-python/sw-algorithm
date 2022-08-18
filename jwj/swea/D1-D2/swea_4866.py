T = int(input())

for tc in range(1, T+1):

    strs = input()
    check_dic = {'(' : ')', '{' : '}'}
    stack = []
    result = 1

    for char in strs:
        if char == '{' or char == '(':
            stack.append(char)

        elif char == '}' or char == ')':
            if stack:
                if check_dic.get(stack[-1]) == char:
                    stack.pop()
                else:
                    result = 0
                    break
            else:
                result = 0
                break

    if stack:
        result = 0

    print(f'#{tc} {result}')
