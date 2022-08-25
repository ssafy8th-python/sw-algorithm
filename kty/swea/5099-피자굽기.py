import sys

sys.stdin = open("input_5099.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    pizza = list(enumerate(map(int, input().split()), 1))

    in_oven = pizza[:n]
    out_oven = pizza[n:]

    while len(in_oven) > 1:
        num, cheese = in_oven.pop(0)
        cheese //= 2
        if cheese != 0:
            in_oven.append((num, cheese))
        else:
            if out_oven:
                in_oven.append(out_oven.pop(0))

    print(f'#{tc} {in_oven[0][0]}')




