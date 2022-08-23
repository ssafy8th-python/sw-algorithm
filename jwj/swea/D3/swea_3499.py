T = int(input())

for tc in range(1, T+1):
    N = int(input())

    strs = input().split()

    print(f'#{tc} ', end='')
    if N % 2:
        s1 = strs[:N//2+1]
        s2 = strs[N//2+1:]

        for idx in range(N//2):
            print(s1[idx], s2[idx], end=' ')
        print(s1[-1])

    else:
        s1 = strs[:N//2]
        s2 = strs[N//2:]

        for idx in range(N//2):
            print(s1[idx], s2[idx], end=' ')
        print()


