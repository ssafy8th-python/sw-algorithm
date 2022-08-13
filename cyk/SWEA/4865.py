import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    s = list(input())
    check = list(input())
    dict_check = { i : check.count(i) for i in s }
    print(f'#{tc} {max(dict_check.values())}')
