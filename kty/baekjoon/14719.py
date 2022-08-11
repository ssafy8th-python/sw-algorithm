h, w = map(int, input().split())
buildings = list(map(int, input().split()))

water = 0
for i in range(1, w - 1):
    left_max = max(buildings[:i])
    right_max = max(buildings[i+1:])
    result = min(left_max, right_max)
    if result > buildings[i]:
        water += result - buildings[i]

print(water)
