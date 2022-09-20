T = int(input())


def htob(h):
    s = ""
    for n_str in h:
        if n_str.isdecimal():
            n_str = int(n_str)
        else:
            n_str = ord(n_str) - 55

        for i in range(3, -1, -1):
            s += '1' if n_str & (1 << i) else '0'

    return s


for test_case in range(1, T+1):
    N, h_num = input().split()

    result = htob(h_num)

    print(f'#{test_case} {result}')
