n = int(input())
num1, num2 = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n+1)]

def bfs(start, end):
    q = [start]
    visited = [0] * (n+1)
    while q:
        x = q.pop(0)
        visited[x] = 1
        for w in arr[x]:
            if not visited[w]:
                visited[w] = visited[x]+1
                q.append(w)
                if w == end:
                    return visited[w]+1
    return -1

for _ in range(m):
    p, c = map(int, input().split())
    arr[p].append(c)
    arr[c].append(p)
print(bfs(num1, num2))