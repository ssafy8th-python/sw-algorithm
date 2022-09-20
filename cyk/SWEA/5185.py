# 이진수
# 16진수 1자리는 2진수는 4자리로 표시된다
# N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램을 만드시오

# a = 0b1101
# result = ''
# for i in range(4):
#     if a&8:
#         result += '1'
#     else :
#         result += '0'
#     # a *= 2
#     a <<= 1
# print(result)

import sys
sys.stdin = open("sample_input (6).txt", "r")

T = int(input())
for tc in range(1, 1+T):
    N, hex = input().split()
    print(f'#{tc}', end=" ")
    for i in hex:
        b = format(int(i, base=16), 'b')
        print(b.zfill(4), end="")
    print()


