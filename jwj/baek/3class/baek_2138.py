import sys

input = sys.stdin.readline


def three(cur, idx):
    cur[idx-1] = not cur[idx-1]
    cur[idx] = not cur[idx]
    cur[idx+1] = not cur[idx+1]


def two(cur, idx1, idx2):
    cur[idx1] = not cur[idx1]
    cur[idx2] = not cur[idx2]


N = int(input())

cur = list(map(int, input().rstrip()))
next_lights = list(map(int, input().rstrip()))

r1 = cur[::]
r2 = cur[::]
c = [r1, r2]
res = 200000

start = 0

two(r2, 0, 1)

for idx in range(2):
    cnt = idx
    i = 0
    for i in range(1, N-1):
        if c[idx][i-1] != next_lights[i-1]:
            three(c[idx], i)
            cnt += 1

    if c[idx][i] != next_lights[i]:
        two(c[idx], i, i+1)
        cnt += 1

    if c[idx] == next_lights:
        if res > cnt:
            res = cnt


if res == 200000:
    print(-1)
else:
    print(res)
