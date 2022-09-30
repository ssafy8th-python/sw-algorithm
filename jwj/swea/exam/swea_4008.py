import math

T = int(input())

INF = 100000000


def perm(r, s):
    global maxV, minV

    if r == N:
        if maxV < s:
            maxV = s

        if minV > s:
            minV = s

    else:
        for i in range(4):
            if exp[i] != 0:
                if i == 0:
                    tmp = s + num_arr[r]
                elif i == 1:
                    tmp = s - num_arr[r]
                elif i == 2:
                    tmp = s * num_arr[r]
                else:
                    tmp = s / num_arr[r]
                    if s < 0:
                        tmp = math.ceil(tmp)
                    else:
                        tmp = math.floor(tmp)

                exp[i] -= 1
                perm(r+1, tmp)
                exp[i] += 1


for test_case in range(1, T+1):
    N = int(input())

    exp = list(map(int, input().split()))

    num_arr = list(map(int, input().split()))

    minV = INF

    maxV = -INF

    if sum(exp) == 0:
        for num in num_arr:
            if minV > num:
                minV = num

            if maxV < num:
                maxV = num
    else:
        perm(1, num_arr[0])

    print(f'#{test_case} {maxV - minV}')
