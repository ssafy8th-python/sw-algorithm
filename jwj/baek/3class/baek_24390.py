from collections import deque

m, s = map(int, input().split(":"))

time = m * 60 + s

q = deque()

q.append((0, 0, 1))

while q:
    second, cnt, start = q.popleft()

    if second > time:
        continue

    if second == time:
        print(cnt + start)
        break

    if second == 0:
        q.append((30, cnt + 1, 0))
    else:
        q.append((second + 30, cnt + 1, start))

    q.append((second + 600, cnt + 1, start))
    if time - second < 600:
        q.append((second + 60, cnt + 1, start))
    if time - second < 60:
        q.append((second + 10, cnt + 1, start))
