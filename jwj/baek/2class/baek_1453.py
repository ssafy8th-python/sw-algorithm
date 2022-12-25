pc = [0] * 101

N = int(input())
people = list(map(int, input().split()))
res = 0

for p in people:
    if pc[p]:
        res += 1
    else:
        pc[p] = 1

print(res)


