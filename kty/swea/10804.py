T = int(input())

for tc in range(1, T+1):
    s = input()
    mirror = []
    for i in range(len(s)-1, -1, -1):
        if s[i] == 'b':
            mirror.append('d')
        elif s[i] == 'd':
            mirror.append('b')
        elif s[i] == 'p':
            mirror.append('q')
        elif s[i] == 'q':
            mirror.append('p')

    print(f"#{tc} {''.join(mirror)}")