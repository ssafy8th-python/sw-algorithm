import sys

sys.stdin = open("input_3499.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    card = input().split()

    st = 0
    ed = n-1
    mid = (st+ed)//2 + 1
    left = card[:mid]
    right = card[mid:]

    i = 0
    j = 0
    result = []
    while i < len(left) and i < len(right):
        result.append(left[i])
        result.append(right[i])
        i += 1
    if len(left) > len(right):
        result.append(left[-1])

    print(f"#{tc} {' '.join(result)}")