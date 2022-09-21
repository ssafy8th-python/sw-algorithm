def npr(num, r, cnt):
    global result

    if cnt == n:
        value = int(''.join(num))

        if value > result:
            result = value

    elif r == num_len:
        return

    else:
        for i in range(num_len):

            num[r], num[i] = num[i], num[r]
            if r == i:
                npr(num, r+1, cnt)
            else:
                npr(num, r+1, cnt+1)
            num[r], num[i] = num[i], num[r]


T = int(input())

for test_case in range(1, T+1):
    num, n = input().split()
    num = list(num)

    # 숫자 길이
    num_len = len(num)

    n = int(n)
    result = 0

    remainder = 0

    if num_len < n:
        remainder = n - num_len
        n = num_len

    npr(num, 0, 0)

    if remainder % 2:
        num[-1], num[-2] = num[-2], num[-1]

    print(f'#{test_case} {result}')