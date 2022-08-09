T = 10

for tc in range(1, T + 1):
    buildings = int(input())
    b_h = list(map(int, input().split()))
    sunny = 0

    for i in range(2, buildings - 2):
        if b_h[i] > b_h[i - 2] and b_h[i] > b_h[i - 1] and b_h[i] > b_h[i + 1] and b_h[i] > b_h[i + 2]:
            max_height = 0
            for j in (b_h[i - 2], b_h[i - 1], b_h[i + 1], b_h[i + 2]):
                if j > max_height:
                    max_height = j

            sunny += b_h[i] - max_height

    print(f'#{tc} {sunny}')