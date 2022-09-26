from collections import deque


def bfs(limit, start, destination):
    visited = [False] * (limit + 1)

    q = deque()
    q.append((start, 0))

    while q:
        stair, cnt = q.popleft()

        if stair > limit or stair <= 0 or visited[stair]:
            continue
        else:
            visited[stair] = True

        if stair == destination:
            return cnt

        q.append((stair + U, cnt+1))
        q.append((stair - D, cnt+1))

    return 'use the stairs'


F, S, G, U, D = map(int, input().split())

print(bfs(F, S, G))
