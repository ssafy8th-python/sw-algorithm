import sys
input = sys.stdin.readline

s = list(input().rstrip())

key = list(input().rstrip())

k_len = len(key)

stack = []

for char in s:
    stack.append(char)

    if char == key[-1] and len(stack) >= k_len:

        for idx in range(1, k_len+1):
            if key[-idx] != stack[-idx]:
                break
        else:
            for _ in range(k_len):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")
