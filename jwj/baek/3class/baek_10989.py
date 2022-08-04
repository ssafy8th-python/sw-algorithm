import sys
input = sys.stdin.readline

res = {}
max_value = 0
for _ in range(int(input())):
    num = int(input())

    check = res.get(num, False)

    if check:
        res[num] += 1
    else:
        res[num] = 1

    if max_value < num:
        max_value = num


for i in range(max_value+1):
    num = res.get(i, False)
    if num:
        for _ in range(num):
            print(i)