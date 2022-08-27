def dfs(card, cnt):
    global minV

    if minV <= cnt:
        return

    if card == asc_check or card == des_check:
        if minV > cnt:
            minV = cnt
    else:

        k = (N // 2) - 1
        # 반 + 1
        for idx in range(0, N//2):
            tmp_card = card[::]
            for i in range(idx+1):
                n_k = k + i * 2
                tmp_card[n_k], tmp_card[n_k+1] = tmp_card[n_k+1], tmp_card[n_k]
            print(tmp_card)
            dfs(tmp_card, cnt+1)
            k -= 1
        print()

        k = 1
        for idx in range(N//2-1, 0, -1):
            tmp_card = tmp_card[::]
            for i in range(idx):
                n_k = k + i * 2
                tmp_card[n_k], tmp_card[n_k+1] = tmp_card[n_k+1], tmp_card[n_k]
            print(tmp_card)
            dfs(tmp_card, cnt+1)
            k += 1
        print()
        
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    cards = list(map(int, input().split()))

    visited = [0] * (N)

    asc_check = [i for i in range(1, N+1)]
    des_check = [i for i in range(N, 0, -1)]

    minV = 6

    dfs(cards, 0)

    if minV > 5:
        minV = -1

    print(f'#{tc} {minV}')
