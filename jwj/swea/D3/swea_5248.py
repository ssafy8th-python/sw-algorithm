T = int(input())


def find_set(x):
    while x != lst[x]:
        x = lst[x]
    return x


for test_case in range(1, T+1):
    N, M = map(int, input().split())

    lst = [i for i in range(N + 1)]

    arr = list(map(int, input().split()))

    for i in range(M):
        n1 = find_set(arr[i * 2])
        n2 = find_set(arr[i * 2 + 1])
        lst[n2] = n1

    result = 0
    for i in range(1, N+1):
        if i == lst[i]:
            result += 1

    print(f'#{test_case} {result}')