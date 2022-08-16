T = int(input())

for tc in range(1, T+1):
    lst = [input() for _ in range(5)]

    result = ''

    current_idx = 0

    max_idx = 0

    for strs in lst:
        if len(strs) > max_idx:
            max_idx = len(strs)

    for idx in range(max_idx):
        for strs in lst:
            if len(strs) <= idx:
                continue
            result += strs[idx]

    print(f'#{tc} {result}')
