import sys

sys.stdin = open("input_4047.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    card = input()
    card_pack = {'S' :[], 'D' :[], 'H':[], 'C':[]}

    for i in range(0, len(card), 3):
        c = card[i]
        n = card[i+1:i+3]
        if n not in card_pack[c]:
            card_pack[c].append(n)
        else:
            print(f'#{tc} ERROR')
            break

    else:
            print(f'#{tc}', end=" ")
            for i in card_pack:
                print(13 - len(card_pack[i]), end=' ')
            print()

