# 연결 요소의 개수
# 방향 없는 그래프가 주어졌을 때 연결 요소의 개수를 구하는 프로그램 작성

def dfs(v):
    st = [v]
    visited[v] = True
    while st:
        for w in arr[v]:
            if not visited[w]:
                st.append(v)
                v = w
                visited[v] = True
                break
        else:
            v = st.pop()

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    p, c = map(int, input().split())
    arr[p].append(c)
    arr[c].append(p)

visited = [False] * (N+1)
cnt = 0
for i in range(1, N+1):
    if visited[i] == False:
        cnt += 1
        dfs(i)
print(cnt)
