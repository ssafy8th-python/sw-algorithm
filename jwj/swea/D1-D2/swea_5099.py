T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    C_lst = list(map(int, input().split()))

    q = []
    for idx in range(N):
        q.append((C_lst[idx], idx))

    while q:
        C, i = q.pop(0)

        if C != 0:
            C //= 2
            if C == 0:
                if idx < M-1:
                    idx += 1
                    q.append((C_lst[idx], idx))
            else:
                q.append((C, i))

    print(f'#{tc} {i+1}')
