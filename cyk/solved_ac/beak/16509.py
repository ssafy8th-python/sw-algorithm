# 장군
# 상이 왕에게 도달할 수 있는 최소 이동 횟수를 출력한다. 만약 도달할 수 없다면 -1을 출력한다.
from collections import deque

def bfs(r, c):
     visited = [[0]*9 for _ in range(10)]
     q = deque([(r,c)])
     visited[r][c] = 1
     while q:
          cr, cc = q.popleft()
          if cr == kr and cc == kc:
               return visited[cr][cc]-1
          for dr, dc in dir:
               nr, nc = dr+cr, dc+cc
               if 0 <= nr < 10 and 0 <= nc < 9 and not visited[nr][nc]:
                    if dr < 0 and dc < 0:    # - - => + +
                         if (nr+2 == kr and nc+2 == kc) or (nr+1 == kr and nc+1 == kc):
                              continue
                    elif dr > 0 and dc < 0:  # + - => - +
                         if (nr-2 == kr and nc+2 == kc) or (nr-1 == kr and nc+1 == kc):
                              continue
                    elif dr < 0 and dc > 0:  # - + => + -
                         if (nr+2 == kr and nc-2 == kc) or (nr+1 == kr and nc-1 == kc):
                              continue
                    elif dr > 0 and dc > 0:  # + + => - -
                         if (nr-2 == kr and nc-2 == kc) or (nr-1 == kr and nc-1 == kc):
                              continue
                    visited[nr][nc] = visited[cr][cc] + 1
                    q.append((nr, nc))

     return -1


sr, sc = map(int, input().split())
kr, kc = map(int, input().split())
dir = [[-2,-3],[-3,-2],[3,2],[2,3],[-2,3],[3,-2],[-3,2],[2,-3]]
print(bfs(sr, sc))
