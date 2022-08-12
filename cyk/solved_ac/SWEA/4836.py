T = int(input())
for tc in range(1, T+1):
    dict_1 = {1 :[]}
    dict_2 = {2 :[]}

    n = int(input())

    for _ in range(n):
        a, b, c, d, e = map(int, input().split())
        if e == 1:
            for i in range(a, c+1):
                for j in range(b, d+1):
                    dict_1[e].append((i,j))
        if e == 2:
            for i in range(a, c + 1):
                for j in range(b, d + 1):
                    dict_2[e].append((i, j))
    print(f'#{tc} {len(set(dict_1[1])&set(dict_2[2]))}')