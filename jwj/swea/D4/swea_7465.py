T = int(input())


def find_set(x):
    while x != lst[x]:
        x = lst[x]
    return x


def union(x, y):
    lst[find_set(y)] = find_set(x)


for test_case in range(1, T+1):
    N, M = map(int, input().split())

    lst = [i for i in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        union(x, y)

    result = 0
    for i in range(1, N+1):
        if i == lst[i]:
            result += 1

    print(f'#{test_case} {result}')