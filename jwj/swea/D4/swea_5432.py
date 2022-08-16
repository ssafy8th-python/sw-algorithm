T = int(input())

for tc in range(1, T+1):
    stack = []
    bracket = input()

    res = 0     # 결과 값
    cnt = 0     # 자를 막대기

    is_left = True
    for b in bracket:
        if b == '(':
            stack.append(b)

            res += 1
            cnt += 1

            is_left = True
        else:
            stack.pop()
            cnt -= 1

            if is_left:
                res -= 1
                res += cnt

            is_left = False

    print(f'#{tc} {res}')
