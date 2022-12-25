
test_case = 1

while True:
    # 적정 체중, 실제 체중
    o, w = map(int, input().split())

    # 끝 나는 경우
    if o == 0 and w == 0:
        break

    status = ':-('

    while True:
        action, n = input().split()

        # 한 시나리오가 끝나는 경우
        if action == '#' and n == '0':
            if o / 2 < w < o * 2:
                status = ':-)'
            break

        if status == 'RIP':
            continue

        n = int(n)

        if action == 'F':
            w += n
        else:
            w -= n

        # 펫 사망
        if w <= 0:
            status = "RIP"

    print(test_case, status)
    test_case += 1



