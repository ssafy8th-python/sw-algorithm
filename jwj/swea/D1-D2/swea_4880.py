def sp(start, end):
    if start == end:
        return end

    mid = (start + end) // 2
    left = sp(start, mid)
    right = sp(mid+1, end)

    if card[left] == card[right]:
        return left

    elif card[left] == 1:
        if card[right] == 2:
            return right
        else:
            return left

    elif card[left] == 2:
        if card[right] == 1:
            return left
        else:
            return right

    elif card[left] == 3:
        if card[right] == 1:
            return right
        else:
            return left


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    card = list(map(int, input().split()))

    res = sp(0, N-1)

    print(f'#{tc} {res + 1}')
