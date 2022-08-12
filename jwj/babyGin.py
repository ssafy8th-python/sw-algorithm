N = int(input())

card = [0] * 12


for _ in range(6):      # 6장
    card[N % 10] += 1
    N //= 10

run = 0
te = 0
i = 0
while i < 12:
    if card[i] >= 3:
        run += 1
        card[i] -= 3
        continue

    if card[i] >= 1 and card[i+1] >= 1 and card[i+2] >= 1:
        te += 1
        card[i] -= 1
        card[i+1] -= 1
        card[i+2] -= 1
        continue

    i += 1

if run + te == 2:
    print('babyGin')
