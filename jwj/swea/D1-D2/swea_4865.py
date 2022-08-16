T = int(input())

for tc in range(1, T+1):
    str1 = list(input())
    str2 = input()

    maxV = 0

    # for char1 in str1:
    #     cnt = 0
    #     for char2 in str2:
    #         if char1 == char2:
    #             cnt += 1
    #
    #     if maxV < cnt:
    #         maxV = cnt

    for char1 in str1:
        cnt = str2.count(char1)

        if maxV < cnt:
            maxV = cnt

    print(f'#{tc} {maxV}')