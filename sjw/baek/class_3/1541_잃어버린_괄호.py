# 1541 잃어버린 괄호
# 주소: https://www.acmicpc.net/problem/1541

# 제출한 답
import sys
input = sys.stdin.readline

lst = list(input().rstrip().split('-'))

result = sum(map(int, lst[0].split('+')))

for i in lst[1:]:
    result -= sum(map(int, i.split('+')))

print(result)


# 다른 답
s = input()
o = 0
c = 0
m = 1
for e in s:
    if e in "+-":
        o += m * c
        c = 0
        if e == "-":
            m = -1
        continue
    c = c * 10 + int(e)
o += m * c
print(o)
