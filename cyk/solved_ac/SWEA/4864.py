import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    input_str = input()
    check_str = input()
    if input_str in check_str:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')
