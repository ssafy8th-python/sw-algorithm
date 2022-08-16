import sys

sys.stdin = open("input_4865.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    arr1 = list(set(input()))
    arr2 = input()
    collection = {}

    for i in arr1:
        for j in arr2:
            if i == j:
                if i in collection:
                    collection[i] += 1
                else:
                    collection[i] = 1

    result = sorted(collection.items(), key = lambda x: x[1], reverse=True)
    maxV = 0
    for alpha, cnt in result:
        if cnt > maxV:
            maxV = cnt

    print(f'#{tc} {maxV}')