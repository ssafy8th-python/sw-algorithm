import sys

sys.stdin = open("input_1860.txt", "r")

def fish(cus, n, m, k):                     # 붕어빵 점화식
    for i in range(n):                      # 손님이 오는 시간이 time 일 때
        if (cus[i]//m * k) - (i+1) < 0:     # 해당 손님이 올 때까지 만들 수 있는 붕어 빵의 개수는
            return 'Impossible'             # (time//M) * K    # M은 몇초마다 만들 수있나 K는 한번에 몇개 만드나
    return 'Possible'                       # 해당 시간 손님이 올때 만들 수 있는 붕어빵의 개수엣
                                            # 손님 배열의 해당 인덱스만큼 앞에서 붕어빵이 팔렸을 것 이기 때문에
                                            # 해당 시간대의 손님이 올때 만들 수 있는 붕어빵의 개수에서 - (i + 1)

def sort_customer(lst, N):                  # 손님 배열 오름차순으로 정렬
    for i in range(0, N-1):
        minP = i
        for j in range(i+1, N):
            if lst[j] < lst[minP]:
                minP = j
        lst[minP], lst[i] = lst[i], lst[minP]

    return lst

T = int(input())
for tc in range(1, T + 1):
    N, M ,K = map(int, input().split())
    customer = list(map(int, input().split()))
    sonnim = sort_customer(customer, N)

    print(f'#{tc} {fish(sonnim, N, M, K)}')
