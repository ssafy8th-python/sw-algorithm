import math

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    res = N ** (1/3)
    res1 = math.ceil(res)

    if math.isclose(res, res1):
        print(f'#{test_case} {res1}')
    else:
        print(f'#{test_case} -1')