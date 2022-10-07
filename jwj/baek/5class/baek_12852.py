from collections import deque

INF = 1000000

N = int(input())

q = deque()
q.append((1, []))
visited = [False] * 1000001
visited[1] = True

while q:
    num, lst = q.popleft()

    if num > N:
        continue

    lst.append(num)

    if num == N:
        print(len(lst) - 1)
        lst.reverse()
        print(*lst)
        break

    n_3 = num * 3
    if n_3 <= N and not visited[n_3]:
        visited[n_3] = True
        q.append((n_3, lst[:]))

    n_2 = num * 2
    if n_2 <= N and not visited[n_2]:
        visited[n_2] = True
        q.append((n_2, lst[:]))

    n_1 = num + 1
    if n_1 <= N and not visited[n_1]:
        visited[n_1] = True
        q.append((n_1, lst[:]))
