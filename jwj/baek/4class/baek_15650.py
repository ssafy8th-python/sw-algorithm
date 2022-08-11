N, M = map(int, input().split())

result = []
for i in range(1 << N):
    lst = []
    resStr = ''
    for j in range(N):

        if i & (1 << j):
            lst.append(j+1)
    if len(lst) == M:
        resStr = list(map(str, lst))
        resStr = ''.join(resStr)
        result.append(resStr)

result.sort()

for strs in result:
    for char in strs:
        print(char, end=' ')
    print()


