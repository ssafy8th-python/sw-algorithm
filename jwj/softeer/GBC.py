

N, M = map(int, input().split())

limit_elv = [0] * 101
cur_elv = [0] * 101

cur_p = 0
for _ in range(N):
    m, s = map(int, input().split())

    for i in range(cur_p, cur_p + m):
        limit_elv[i] = s
    cur_p += m

cur_p = 0
for _ in range(M):
    m, s = map(int, input().split())

    for i in range(cur_p, cur_p + m):
        cur_elv[i] = s
    cur_p += m

limit = [0]
for i in range(101):
    if limit_elv[i] < cur_elv[i]:
        limit.append(cur_elv[i] - limit_elv[i])

print(max(limit))