import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    n = int(input())

    pictures = [list(map(int, input().split())) for _ in range(2)]

    if n > 1:
        pictures[0][1] += pictures[1][0]
        pictures[1][1] += pictures[0][0]

    for idx in range(2, n):
        pictures[0][idx] += max(pictures[1][idx-1], pictures[1][idx-2])
        pictures[1][idx] += max(pictures[0][idx-1], pictures[0][idx-2])

    print(max(pictures[0][-1], pictures[1][-1]))
