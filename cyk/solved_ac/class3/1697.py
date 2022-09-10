# 숨바꼭질
# 위치가 X일때 걸으면 1초 후 X-1 혹은 X+1 / 순간이동을 한다면 1초 후 2*X
# 동생을 찾을 수 있는 가장 빠른 시간 => BFS
from collections import deque
N, K = map(int, input().split())

def bfs(X):
    q = deque([X])
    while q:
        X = q.popleft()
        if X == K:                          # 종료 조건
            return visited[X]
        for calc in [X-1, X+1, X*2]:        # 정점에서 할 일
            if 0 <= calc <= max and visited[calc] == 0:
                visited[calc] = visited[X] + 1
                q.append(calc)


max = 100000
visited = [0] * (max+1)
print(bfs(N))
