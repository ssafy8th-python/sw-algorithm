# n 개 중 r개를 선택하는 순열     nPr

input_data = [1, 2, 3, 4, 5, 6]


def f(lst, r, c):
    if r == c:
        print(lst)
    else:
        for i in range(len(input_data)):
            if not used[i]:
                lst[r] = input_data[i]
                used[i] = True
                f(lst, r+1, c)
                lst[r] = 0
                used[i] = False


lst = [0] * len(input_data)

used = [False] * len(input_data)

f(lst, 0, 3)

