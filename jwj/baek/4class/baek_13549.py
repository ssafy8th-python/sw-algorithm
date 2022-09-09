from collections import deque

N, K =  map(int, input().split())

q = deque()

q.append((N, 0))

visited = [-1] * 100001

while q:
    num, cnt = q.popleft()

    if num == K:
        break

    a = num * 2
    if 0 <= a <= 100000 and visited[a] == -1:
        q.append((a, cnt))
        visited[a] = cnt
    
    b = num - 1
    if 0 <= b <= 100000 and visited[b] == -1:
        q.append((b, cnt + 1))
        visited[b] = cnt + 1
    
    c = num +1
    if 0 <= c <= 100000 and visited[c] == -1:
        q.append((c, cnt + 1))
        visited[c] = cnt + 1
    
print(cnt)
