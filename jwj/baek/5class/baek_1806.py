N, S = map(int, input().split())

p = list(map(int, input().split()))

lp = 0
rp = 1
minV = 100000
cnt = 1
cur = p[0]

while rp <= N:
    # print(cur)
    # S 이상인 경우
    if cur >= S:
        if minV > cnt:
            minV = cnt

        cur -= p[lp]
        lp += 1
        cnt -= 1

    else:
        if rp < N:
            cur += p[rp]
        rp += 1
        cnt += 1

if minV == 100000:
    print(0)
else:
    print(minV)
