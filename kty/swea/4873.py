import sys

sys.stdin = open("input_4873.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    sentence = list(input())
    N = len(sentence)
    stack = []
    for i in range(0, N):
        if not stack or stack[-1] != sentence[i]:
            stack.append(sentence[i])

        elif stack and stack[-1] == sentence[i]:
            stack.pop()
    print(f'#{tc} {len(stack)}')