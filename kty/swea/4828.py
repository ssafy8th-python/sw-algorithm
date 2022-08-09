import sys

sys.stdin = open("input_4828.txt", "r")

T = int(input())
for tc in range(1, T+1):
    num = int(input())
    num_list = list(map(int, input().split()))

    max_num = num_list[0]
    min_num = num_list[0]
    for i in num_list:
        if i > max_num:
            max_num = i
        elif i < min_num:
            min_num = i

    print(f'#{tc} {max_num-min_num}')


