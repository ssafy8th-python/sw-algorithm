import sys

sys.stdin = open("gidung.txt", "r")

n = int(input())
col = [list(map(int, input().split())) for _ in range(n)]
col.sort()

maxW = 0
for i in range(n):
    if col[i][0] > maxW:
        maxW = col[i][0]

world = [0] * (maxW + 1)

for i in col:
    world[i[0]] = i[1]

k = world.index(max(world))

left = world[:k]
right = world[k:]
right.reverse()

result = 0
left_max = 0
for i in left:
    if i > left_max:
        left_max = i
    result += left_max

right_max = 0
for j in right:
    if j > right_max:
        right_max = j
    result += right_max

print(result)
