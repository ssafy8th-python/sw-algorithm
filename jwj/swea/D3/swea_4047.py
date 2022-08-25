T = int(input())

for tc in range(1, T+1):
    card_dict = {'S': [0] * 14, 'D': [0] * 14, 'H': [0] * 14, 'C': [0] * 14}
    cards = list(input())

    check = False
    for idx in range(0, len(cards), 3):
        kind = cards[idx]
        num = int(''.join(cards[idx+1:idx+3]))

        if card_dict[kind][num] == 1:
            check = True
            break
        else:
            card_dict[kind][num] += 1

    if check:
        print(f'#{tc} ERROR')
    else:
        print(f'#{tc}', end=' ')
        for char in ['S', 'D', 'H', 'C']:
            print(13-sum(card_dict[char]), end=' ')
        print()
