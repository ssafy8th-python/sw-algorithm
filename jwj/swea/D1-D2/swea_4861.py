T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [input() for _ in range(N)]

    result = False

    for strs in lst:
        for cnt in range(N-M+1):
            tmp_strs = strs[cnt:cnt+M]
            if tmp_strs == tmp_strs[::-1]:
                result = tmp_strs
                break


    if not result:
        for i in range(N):
            for cnt in range(N-M+1):
                strs = ''
                for j in range(cnt, cnt+M):
                    strs += lst[j][i]
                if strs == strs[::-1]:
                    result = strs
                    break
        if not result:
            break

    print(f'#{tc} {result}')