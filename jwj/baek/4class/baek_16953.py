def rec(num, cnt):
    global min_cnt

    if min_cnt <= cnt:
        return

    if num > B:
        return
    elif num == B:
        if min_cnt > cnt:
            min_cnt = cnt
            return

    rec(num * 2, cnt + 1)
    rec(num * 10 + 1, cnt + 1)

A, B = map(int, input().split())

min_cnt = 100000000

rec(A, 1)

if min_cnt == 100000000:
    min_cnt = -1

print(min_cnt)
