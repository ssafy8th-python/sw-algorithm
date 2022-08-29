import sys

n = int(sys.stdin.readline())
dice = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

match = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

maxV = 0
for i in range(6):
    sumV = 0
    num = [1, 2, 3, 4, 5, 6]
    floor = dice[0][i]
    celling = dice[0][match[i]]
    num.remove(floor)
    num.remove(celling)
    sumV += max(num)
    for j in range(1, n):
        num = [1, 2, 3, 4, 5, 6]
        floor = celling
        num.remove(floor)
        celling = dice[j][match[dice[j].index(floor)]]
        num.remove(celling)
        sumV += max(num)

    if sumV > maxV:
        maxV = sumV

print(maxV)
