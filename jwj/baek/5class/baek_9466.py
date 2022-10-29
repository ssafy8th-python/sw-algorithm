import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e7))


def dfs(x):
    global result

    visited[x] = True
    cycle.append(x)

    student = students[x]

    if visited[student]:
        if student in cycle:
            result += cycle[cycle.index(student):]
            return

    else:
        dfs(student)


T = int(input())

for _ in range(T):
    n = int(input())
    students = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    result = []

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - len(result))
