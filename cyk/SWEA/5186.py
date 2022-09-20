# 이진수 2
# N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자 출력
# 13자리 이상 필요한 경우에는 'overflow'를 출력
import sys
sys.stdin = open("sample_input (6).txt", "r")
T = int(input())
for tc in range(1, 1+T):
    N = input()
    num = float(N)
    res = ''
    for i in range(1,13):
        if num >= 2**(-i):
            num -= 2**(-i)
            res += '1'
        else:
            res += '0'
        if num == 0:
            break

    print(f'#{tc}', end=' ')
    if num:
        print('overflow', end='')
    else:
        for elem in res:
            print(int(elem), end='')
    print()

    # 다른 풀이
    # import math
    #
    # t = int(input())
    # for tc in range(1, t + 1):
    #     n = float(input())
    # result = ''
    # for _ in range(12):
    #     if n == 0:
    #         break
    # result += str(math.floor(n * 2))
    # n = (n * 2) % 1
    #
    # if n != 0:
    #     print(f'#{tc} overflow')
    # else:
    #     print(f'#{tc} {result}')