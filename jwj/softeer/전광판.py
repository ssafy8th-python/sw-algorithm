def switch(A_lst, B_lst):
    value = 0
    for i in range(len(B_lst)):
        for index in range(7):
            if A_lst[i][index] != B_lst[i][index]:
                value += 1
    diff = len(A_lst) - len(B_lst)
    for i in range(1, diff+1):
        i *= -1
        value += sum(A_lst[i])

    return value


T = int(input())

# 전강판을 리스트로 가진다.
light = [[1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 1, 0, 1, 1], [1, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1],
         [1, 1, 0, 1, 1, 0, 1], [1, 1, 1, 1, 1, 0, 1], [1, 1, 0, 0, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1, 1]]

for _ in range(T):
    A, B = list(input().split())

    A_light = []
    B_light = []

    for a in A:
        a = int(a)
        A_light.append(light[a])

    for b in B:
        b = int(b)
        B_light.append(light[b])

    A = int(A)
    B = int(B)

    A_light.reverse()
    B_light.reverse()

    if A < B:
        result = switch(B_light, A_light)
    else:
        result = switch(A_light, B_light)

    print(result)