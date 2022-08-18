stack = []
N = int(input())
for num in range(N):
    K = int(input())
    if K != 0:
        stack.append(K)
    else:
        stack.pop()

print(sum(stack))