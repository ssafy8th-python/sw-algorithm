H, W = map(int, input().split())

block = list(map(int, input().split()))

water = 0

for i in range(1, W-1):
    L_max = max(block[:i])
    R_max = max(block[i+1:])

    minV = min(L_max, R_max)

    if block[i] < minV:
        water += minV - block[i]

print(water)

