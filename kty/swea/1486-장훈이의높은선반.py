import sys

sys.stdin = open("input_1486.txt", "r")

def powerset(i, sumV):
    global minV
    if sumV >= b:
        if minV > sumV:
            minV = sumV
        return

    if i == n:
        return

    else:
        visited[i] = 1
        powerset(i + 1, sumV + people[i])
        visited[i] = 0
        powerset(i + 1, sumV)

T = int(input())
for tc in range(1, T+1):
    n, b = map(int, input().split())
    people = list(map(int, input().split()))
    visited = [-1] * n
    minV = 2000001
    powerset(0, 0)
    print(f'#{tc} {minV-b}')