import sys

sys.stdin = open("input_1234.txt", "r")

T = 10
for tc in range(1, T + 1):
    n, m = list(map(str, input().split()))
    stack = []
    for i in range(len(m)):
        if not stack or stack[-1] != m[i]:
            stack.append(m[i])
        elif stack[-1] == m[i]:
            stack.pop()

    print(f'#{tc} {"".join(stack)}')
