
def calculate(stack):

    if stack[-1] == '-':
        stack.pop()
        b = stack.pop()
        a = stack.pop()
        stack.append(a-b)
    elif stack[-1] == '+':
        stack.pop()
        b = stack.pop()
        a = stack.pop()
        stack.append(a + b)
    elif stack[-1] == '*':
        stack.pop()
        b = stack.pop()
        a = stack.pop()
        stack.append(a * b)
    elif stack[-1] == '/':
        stack.pop()
        b = stack.pop()
        a = stack.pop()
        stack.append(a / b)


def inorder(root):

    if root != 0:
        inorder(tree[root][1])
        inorder(tree[root][2])
        expression.append(tree[root][0])
        calculate(expression)


for test_case in range(1, 11):
    N = int(input())

    tree = [0] * (N + 1)

    for i in range(1, N + 1):
        arr = list(input().split())

        num = len(arr)

        if num == 2:
            tree[int(arr[0])] = (int(arr[1]), 0, 0)

        else:
            tree[int(arr[0])] = (arr[1], int(arr[2]), int(arr[3]))

    expression = []

    inorder(1)

    print(f'#{test_case} {int(expression[0])}')
