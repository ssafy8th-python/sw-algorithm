from collections import deque

for test_case in range(1, 11):
    V, E = map(int, input().split())

    tree = [[] for _ in range(V + 1)]

    arr = list(map(int, input().split()))

    parents = [[] for _ in range(V + 1)]

    visited = [False] * (V + 1)

    for idx in range(E):
        tree[arr[idx * 2]].append(arr[idx * 2 + 1])
        parents[arr[idx * 2 + 1]].append(arr[idx * 2])

    start = 1

    for idx in range(1, V+1):
        if not parents[idx]:
            start = idx
            break

    q = deque()
    q.append(start)

    print(f'#{test_case} ', end="")
    while q:
        v = q.popleft()
        visited[v] = True
        print(v, end=" ")

        destinations = tree[v]

        for destination in destinations:
            for parent in parents[destination]:
                if not visited[parent]:
                    break
            else:
                q.append(destination)

        if not q:
            for idx in range(1, V + 1):
                if not parents[idx] and not visited[idx]:
                    q.append(idx)
                    break

    print()
