

N = int(input())
M = int(input())
result = []

if N == 1:
    N += 1

for i in range(N, M+1):

    for j in range(2, i):
        if i % j == 0:
            break
    else:
        result.append(i)


if result:
    print(sum(result))
    print(result[0])
else:
    print(-1)

