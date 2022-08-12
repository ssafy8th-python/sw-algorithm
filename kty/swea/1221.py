import sys

sys.stdin = open("input_1221.txt", "r")

T = int(input())
for tc in range(1, T+1):
    order, num = list(input().split())
    arr = list(map(str, input().split()))
    N = int(num)
    alphabet = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    result = []

    for i in range(T):
        for j in arr:
            if alphabet[i] == j:
                result.append(j)

    print(order)
    print(*result)
