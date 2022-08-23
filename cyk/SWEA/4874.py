T = int(input())

def forth(s):
    ST = []
    for i in range(0, len(s)-1):     # 피연산자일때
        if s[i].isdigit():
            ST.append(int(s[i]))
        else:               # 연산자일때
            if len(ST) < 2:
                return 'error'
            else:
                if s[i] == '+':
                    a = ST.pop()
                    b = ST.pop()
                    ST.append(a+b)
                elif s[i] == '-':
                    a = ST.pop()
                    b = ST.pop()
                    ST.append(b-a)
                elif s[i] == '*':
                    a = ST.pop()
                    b = ST.pop()
                    ST.append(a*b)
                elif s[i] == '/':
                    a = ST.pop()
                    b = ST.pop()
                    ST.append(b//a)
    if len(ST) != 1:
        return 'error'
    else:
        return ST[-1]

for tc in range(1, T+1):
    s = input().split()
    print(f'#{tc} {forth(s)}')
