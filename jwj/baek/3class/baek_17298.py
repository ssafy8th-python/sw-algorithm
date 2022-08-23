N = int(input())

A_lst = list(map(int, input().split()))

stack = []

result = []

for i in range(N-1, -1, -1):

    if not stack:
        result.append(-1)
        stack.append(A_lst[i])
    elif stack[-1] > A_lst[i]:
        result.append(stack[-1])
        stack.append(A_lst[i])
    else:
        while stack and stack[-1] <= A_lst[i]:
            stack.pop()

        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)

        stack.append(A_lst[i])

for i in range(N-1, -1, -1):
    print(result[i], end=' ')
