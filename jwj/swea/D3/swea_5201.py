T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    goods = list(map(int, input().split()))

    trucks = list(map(int, input().split()))

    goods.sort()
    trucks.sort()

    g, t = N-1, M-1

    result = 0

    while g != -1 and t != -1:
        if goods[g] <= trucks[t]:
            result += goods[g]
            t -= 1
            g -= 1
        else:
            g -= 1

    print(f'#{test_case} {result}')