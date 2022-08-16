for tc in range(10):
    test_case = int(input())

    palindrome = [input() for _ in range(100)]

    maxV = 1

    # 하나 씩 가져옴
    for strs in palindrome:
        # 검사할 개수
        for cnt in range(1, 100):
            if maxV >= cnt:
                continue

            # 시작 위치
            for start in range(100-cnt+1):
                tmp_str = strs[start:start+cnt]
                if tmp_str == tmp_str[::-1]:
                    maxV = cnt
                    break

    # 세로 문장 구하기
    for i in range(100):
        strs = ''
        for j in range(100):
            strs += palindrome[j][i]

        # 검사할 개수
        for cnt in range(1, 100):
            if maxV >= cnt:
                continue

            # 시작 위치
            for start in range(100-cnt+1):
                tmp_str = strs[start:start+cnt]
                if tmp_str == tmp_str[::-1]:
                    maxV = cnt
                    break


    print(f'#{test_case} {maxV}')


