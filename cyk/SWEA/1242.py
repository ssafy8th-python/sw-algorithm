# 암호코드 스캔
import sys
sys.stdin = open("sample_input (6).txt", "r")
# sys.stdin = open("input2.txt", "r")

code = {
    '211': 0,
    '221': 1,
    '122': 2,
    '411': 3,
    '132': 4,
    '231': 5,
    '114': 6,
    '312': 7,
    '213': 8,
    '112': 9
    }

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [input().strip() for _ in range(N)]
    # 16진수를 2진수로 만든다
    newARR = [] # NX(M*4)
    for lst in arr:
        tmp = ''
        for i in lst:
            tmp += format(int(i, base=16), 'b').zfill(4)
        newARR.append(tmp)
    result = []

    for row in range(1,N):
        j = M*4 -1 # 오른 쪽 끝
        # 제일 오른쪽 끝에 있는 1을 찾는다
        while j >= 56:
            if newARR[row][j] == '1' and newARR[row-1][j] == '0':
                tmp = []

                for i in range(8):
                    # 하나 구하기
                    a = [0, 0, 0]

                    while newARR[row][j] == '1':
                        a[2] += 1
                        j-=1

                    while newARR[row][j] == '0':
                        a[1] += 1
                        j-=1

                    while newARR[row][j] == '1':
                        a[0] += 1
                        j-=1
                    while newARR[row][j] == '0':
                        j-=1
                    # a[2] = 1의 개수를 세고
                    # a[1] = 0의 개수를 세고
                    # a[0] = 1의 개수를 센다
                    # a[0] = 0의 개수를 세서 버린다
                    k = min(a)
                    res = ''.join(str(i//k) for i in a)
                    tmp.append(code[res])
                result.append(tmp)
                #     코드 하나를 찾아온다
                # 암호 검증
            else:
                j-=1
    # print(result)
    last_res = 0
    for lst in result:
        plus = 0
        for i in range(len(lst)):
            if i % 2:#홀수
                plus += lst[::-1][i]
            else:
                plus += lst[::-1][i]*3
        if plus % 10:
            continue
        else:
            last_res += sum(lst)
    print(f'#{tc} {last_res}')
