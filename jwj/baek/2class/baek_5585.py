N = int(input())

N = 1000 - N

cnt = 0

if N // 500:
    N = N - 500
    cnt += 1

if N // 100:
    tmp = N // 100
    N = N - (tmp * 100)
    cnt += tmp

if N // 50:
    tmp = N // 50
    N = N - (tmp * 50)
    cnt += tmp

if N // 10:
    tmp = N // 10
    N = N - (tmp * 10)
    cnt += tmp

if N // 5:
    tmp = N // 5
    N = N - (tmp * 5)
    cnt += tmp

if N // 1:
    tmp = N // 1
    N = N - tmp
    cnt += tmp

print(cnt)
