# # 자기 방으로 돌아가기
# '''
# 3
# 4
# 10 20
# 30 40
# 50 60
# 70 80
# 2
# 1 3
# 2 200
# 3
# 10 100
# 20 80
# 30 50
# '''
for tc in range(1, 2):
    dump = int(input())
    s = list(map(int, input().split()))

    maxv = 0
    minv = 101

    for elem in s[1:]:
        if minv > elem:
            minv = elem
        if maxv < elem:
            maxv = elem

    lst = [0] * (maxv + 1)

    for value in s:
        lst[value] += 1

    for i in range(dump):
        lst[minv] -= 1
        lst[minv + 1] += 1
        lst[maxv] -= 1
        lst[maxv - 1] += 1

        if lst[maxv] == 0:
            maxv -= 1
        if lst[minv] == 0:
            minv += 1

        res = maxv - minv
        if res < 2:
            break
    print(lst)
    print(f'#{tc} {res}')

