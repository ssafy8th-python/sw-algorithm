T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    lst = list(input().split())

    index = M % N

    print(f'#{tc} {lst[index]}')
