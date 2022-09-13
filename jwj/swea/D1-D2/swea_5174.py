T = int(input())

for test_case in range(1, T+1):

    E, N = map(int, input().split())

    arr = list(map(int, input().split()))

    parent_node = [0] * (E + 2)

    for i in range(E):
        par = arr[i * 2]
        cha = arr[i * 2 + 1]

        parent_node[cha] = par

    q = [N]

    cnt = 1

    while q:
        check = q.pop(0)

        for i in range(1, E+2):
            if parent_node[i] == check:
                cnt += 1
                q.append(i)

    print(f'#{test_case} {cnt}')