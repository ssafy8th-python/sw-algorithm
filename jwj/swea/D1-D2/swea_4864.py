T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    cnt = len(str2) - len(str1) + 1

    for idx in range(cnt):
        if str1 == str2[idx:idx+len(str1)]:
            print(f'#{tc} 1')
            break
    else:
        print(f'#{tc} 0')


