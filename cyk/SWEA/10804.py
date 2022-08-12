import sys
sys.stdin = open("input (4).txt", "r")

T = int(input())

for tc in range(1, 1+T):
    s = list(input())
    result = []
    for elem in s:
        if elem == 'b':
            result.append('d')
        if elem == 'q':
            result.append('p')
        if elem == 'd':
            result.append('b')
        if elem == 'p':
            result.append('q')
    print(f'#{tc} ', end='')
    print(''.join(result[::-1]))