left = list(input())
right = list(input())

cnt = 0

LCS = [[0] * (len(left) + 1) for _ in range(len(right) + 1)]


for r in range(len(right)):
    for le in range(len(left)):
        if left[le] == right[r]:
            LCS[r+1][le+1] = LCS[r][le] + 1
        else:
            LCS[r+1][le+1] = max(LCS[r+1][le], LCS[r][le+1])

print(LCS[-1][-1])
