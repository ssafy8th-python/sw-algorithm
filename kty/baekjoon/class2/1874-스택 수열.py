N = int(input())
K = [int(input()) for _ in range(N)]

stack = []
result = []
count = 1
for i in K:
    while count <= i:
        stack.append(count)
        result.append('+')
        count += 1

    if stack.pop() == i:
        result.append('-')

    else:
        print('NO')
        exit(0)

print('\n'.join(result))

