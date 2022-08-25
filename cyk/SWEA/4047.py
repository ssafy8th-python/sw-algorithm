# 영준이의 카드 카운팅
'''
3
S01D02H03H04
H02H10S11H02
S10D10H10C01
'''
T = int(input())
for tc in range(1, 1+T):
    s = input()
    S = s.count('S')
    D = s.count('D')
    H = s.count('H')
    C = s.count('C')
    case = []
    for i in range(0, len(s), 3):
        case.append(s[i:i+3])
    print(f'#{tc} ', end='')
    if sorted(list(set(case))) != sorted(case):
        print('ERROR')
    else:
        print(13 - S, 13 - D, 13 - H, 13 - C)