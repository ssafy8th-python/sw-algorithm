N, K = map(int, input().split())

lst = [i for i in range(1, N+1)]

res = []

idx = 0
num = 1

while lst:

    idx %= N

    if num >= K:
        res.append(lst.pop(idx))
        N -= 1
        num = 1
        continue

    num += 1
    idx += 1


print('<', end='')
for num in res[:-1]:
    print(num, end=', ')

print(f'{res[-1]}>', end='')
