T = int(input())

for tc in range(1, T+1):
    N, P = map(int, input().split())

    result = (N // P) ** (P - N % P) * (N // P + 1) ** (N % P)
    print(f'#{tc} {result}')

