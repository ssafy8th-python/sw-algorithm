while True :
    s = sorted(list(map(int, input().split())))
    if s == [0, 0, 0]:
        break
    if (s[0]  + s[1])  > s[2] :
        result = 'right' if (s[0]**2 + s[1] **2) ==s[2]**2 else 'wrong'
        print(result)
    