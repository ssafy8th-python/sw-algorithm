def select(strs):

    strs = list(strs)
    strs.sort()
    strs = ''.join(strs)

    if dict.get(strs, False):
        return
    else:
        dict[strs] = True

    if len(strs) >= M :
        return

    for num in range(1, N+1):
        select(strs + str(num))

N, M = map(int, input().split())

dict = {}

select('')

for key in dict:
    tmp = []
    for char in key:
        tmp.append(char)
    if len(tmp) == M:
        print(*tmp)

