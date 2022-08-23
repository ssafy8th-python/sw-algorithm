# 2309 일곱 난쟁이
# 주소: https://www.acmicpc.net/problem/2309

# 제출한 답
def hundread(k, curSum):
    if len(ans) == 7:
        return
    if curSum > 100:
        return
    if k == 9:
        if curSum == 100 and result.count(1) == 7:
            for i in range(9):
                if result[i] == 1:
                    ans.append(dwarf[i])
    else:
        for i in range(2):
            result[k] = i
            if result[k]:
                hundread(k + 1, curSum + dwarf[k])
            else:
                hundread(k + 1, curSum)


dwarf = [int(input()) for _ in range(9)]
result = [0] * 9
ans = []
hundread(0, 0)
ans.sort()
for i in range(7):
    print(ans[i])
