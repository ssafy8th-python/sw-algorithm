import sys
input = sys.stdin.readline

N = int(input())

tower = list(map(int, input().split()))

result = [0] * N

stack = [(tower[0], 0)]

for idx, t in enumerate(tower[1:], 1):

    while stack:
        if stack[-1][0] < t:
            stack.pop()
        else:
            result[idx] = stack[-1][1]+1
            stack.append((t, idx))
            break
    else:
        stack.append((t, idx))

print(*result)
