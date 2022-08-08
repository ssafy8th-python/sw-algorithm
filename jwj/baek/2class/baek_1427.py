N = list(map(int, input()))

# 최대 개수 10개

# 카운팅 정렬

lst = [0] * 10
tmp = [0] * len(N)

for num in N:
    lst[num] += 1

for idx in range(1, 10):
    lst[idx] += lst[idx-1]

for num in N:
    tmp[-lst[num]] = num
    lst[num] -= 1

for num in tmp:
    print(num, end='')


# for idx in range(9, -1, -1):
#     if lst[idx] != 0:
#         print(str(idx) * lst[idx], end="")