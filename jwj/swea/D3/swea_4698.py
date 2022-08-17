T = int(input())

result = [False, False] + [True] * 1000001

i = 1

while (i * i) < 1000001:
    i += 1

    if result[i]:
        for n in range(i*i, 1000001, i):
            result[n] = False


for tc in range(1, T+1):
    D, A, B = map(int, input().split())
    D = str(D)

    cnt = 0

    for idx in range(A, B+1):
        if result[idx]:
            if D in str(idx):
                cnt += 1

    print(f'#{tc} {cnt}')

