import sys
sys.stdin = open("input_1493.txt", "r")

def amper(a):                       # &계산
    i = 1
    while True:
        if i * (i + 1) // 2 >= a:   # 해당 숫자가 대각선 몇 번째 줄에 있는지
            line = i                # i 까지의 숫자의 합 보다 작거나 같고 i-1까지의 숫자의 합보다 클때
            break                   # 해당 숫자는 i 번째 대각선에 있다.
        i += 1
    ex_line = line - 1              # 해당 숫자의 전 대각선 라인
    sum_xy = line + 1               # i 번째 대각선 위에 있는 숫자 들의 x, y값은 항상 i+1 이다.
    x = a - (ex_line * (ex_line + 1) // 2)  # 해당 수의 x 값은 (해당 수) - ((i-1)까지의 숫자의 합)
    y = sum_xy - x                          # x+y는 항상 i+1 이니깐 i+1값에서 x를 빼주면 y값
    return (x, y)

def star(p2, q2):                           # (#) 계산
    sum_xy = p2 + q2                        # 조립은 분해의 역순
    line = sum_xy - 1
    ex_line = line - 1
    a = p2 + (ex_line * (ex_line + 1) // 2)
    return a

T = int(input())
for tc in range(1, T + 1):
    p, q = map(int, input().split())
    p1 = amper(p)
    q1 = amper(q)
    p2, q2 = p1[0] + q1[0], p1[1]+q1[1]
    print(f'#{tc} {star(p2, q2)}')


    