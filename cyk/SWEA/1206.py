# View
import sys
sys.stdin = open("input (4).txt", "r")

for tc in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))
    k = [-2, -1, 1, 2]
    sumV = 0
    for i in range(2, len(lst)-2):
        temp = []
        if lst[i] - lst[i+k[0]] > 0 and lst[i] - lst[i+k[1]] > 0 and lst[i] - lst[i+k[2]] > 0 and lst[i] - lst[i+k[3]] > 0:
            result = [lst[i] - lst[i+k[0]], lst[i] - lst[i+k[1]], lst[i] - lst[i+k[2]], lst[i] - lst[i+k[3]]]
            minV =result[0]
            for i in range(1,4):
                if result[i] < minV:
                    minV = result[i]
            sumV += minV
    print(f'#{tc} {sumV}')