T = int(input())

for tc in range(1, T+1):
    strs = list(input())

    strs_len = len(strs)

    i = 0

    while i < strs_len-1:

        if strs[i] == strs[i+1]:
            strs.pop(i)
            strs.pop(i)
            i -= 1
        else:
            i += 1

        if i == -1:
            i = 0

        strs_len = len(strs)

    print(f'#{tc} {len(strs)}')

