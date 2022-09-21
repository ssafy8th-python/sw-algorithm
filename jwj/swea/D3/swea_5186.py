def dtob(num):
    result = ''

    idx = 1 / 2

    cnt = 0

    while num != 0 and cnt < 13:
        cnt += 1
        if idx <= num:
            num -= idx
            result += '1'
        else:
            result += '0'

        idx /= 2

    if cnt == 13:
        return 'overflow'
    else:
        return result


T = int(input())

for test_case in range(1, T+1):
    num = float(input())

    result = dtob(num)

    print(f'#{test_case} {result}')