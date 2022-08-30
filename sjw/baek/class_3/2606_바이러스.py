# 2606 바이러스
# 주소: https://www.acmicpc.net/problem/2606

# 제출한 답
# dfs or bfs로 풀이
def dfs(k):
    st = []
    st.append(k)
    result = -1
    while st:
        v = st.pop()
        if visited[v] == 0:
            visited[v] = 1
            result += 1
        for i in graph[v]:
            if visited[i] == 0:
                st.append(i)

    return result


computer = int(input())
n = int(input())

graph = [[] for _ in range(computer + 1)]

for _ in range(n):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [0] * (computer + 1)

print(dfs(1))
