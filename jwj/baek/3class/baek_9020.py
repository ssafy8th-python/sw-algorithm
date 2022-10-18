prime = [False] * 10000

prime[2] = True

for i in range(2, 10000):
    for j in range(2, int(i ** 0.5) + 1):
        if prime[j]:
            if i % j == 0:
                break
    else:
        prime[i] = True

T = int(input())

for test_case in range(1, T+1):
    res_1 = 2
    res_2 = 2
    n = int(input())
    lp = 2
    rp = n - 1

    while lp <= rp:
        if not prime[lp]:
            lp += 1
            continue

        if not prime[rp]:
            rp -= 1
            continue

        n_v = lp + rp

        if n_v == n:
            res_1 = lp
            res_2 = rp
            lp += 1
            rp -= 1
        elif n_v > n:
            rp -= 1
        else:
            lp += 1

    print(res_1, res_2)
