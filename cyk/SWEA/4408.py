# # 자기 방으로 돌아가기
'''
3
4
10 20
30 40
50 60
70 80
2
1 3
2 200
3
10 100
20 80
30 50

1
4
10 20
30 40
50 60
70 80
'''


T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    room = [0] * 201
    for _ in range(n):
        s, e = map(int, input().split())
        if s > e:
            s, e = e, s
        if s % 2:
            s = 1+s//2
        else:
            s= s//2
        if e % 2:
            e = 1 + e // 2
        else:
            e = e // 2
        for i in range(s, e+1):
            room[i] += 1
    print(room)
    print(f'#{tc} {max(room)}')
