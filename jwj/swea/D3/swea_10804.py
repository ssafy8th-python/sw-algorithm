T = int(input())

for tc in range(1, T+1):

    mirror = {'b' : 'd', 'd' : 'b', 'q' : 'p', 'p':'q'}

    strs = input()

    strs = strs[::-1]

    result = ''

    for char in strs:
        result += mirror.get(char)


    print(f'#{tc} {result}')
