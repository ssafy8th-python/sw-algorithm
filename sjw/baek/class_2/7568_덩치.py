# 7568 덩치
# 주소: https://www.acmicpc.net/problem/7568

# 제출한 답
n = int(input())

humans = []
grade_lst = []

for _ in range(n):
    humans.append(list(map(int, input().split())))

for i in humans:
    cnt = 1
    for j in humans:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    grade_lst.append(cnt)

print(*grade_lst)