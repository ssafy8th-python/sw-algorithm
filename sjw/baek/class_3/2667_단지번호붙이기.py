# 2667 단지번호붙이기
# 주소: https://www.acmicpc.net/problem/2667

# 제출한 답
import sys
input = sys.stdin.readline

def bfs():
    result = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] and not visited[i][j]:
                q = [(i, j)]
                visited[i][j] = 1
                cnt = 0
                while q:
                    r, c = q.pop(0)
                    cnt += 1
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < N:
                            if arr[nr][nc] and not visited[nr][nc]:
                                q.append((nr, nc))
                                visited[nr][nc] = 1
                result.append(cnt)
    return result


N = int(input())
arr = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dangi = bfs()
dangi.sort()
print(len(dangi))
for i in dangi:
    print(i)
