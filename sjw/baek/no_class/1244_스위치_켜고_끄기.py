# 1244 스위치 켜고 끄기
# 주소: https://www.acmicpc.net/problem/1244

# 제출한 답
import sys
input = sys.stdin.readline

switches = int(input())
init = list(map(int, input().split()))
st_n = int(input())
students = [list(map(int, input().split())) for _ in range(st_n)]

for student in students:
    # 남학생
    if student[0] == 1:
        for i in range(student[1] - 1, switches, student[1]):
            init[i] = (init[i] + 1) % 2
    # 여학생
    else:
        st = 0; ed = 0
        for i in range(switches):
            if 0 <= student[1] - 1 + i < switches and 0 <= student[1] - 1 - i < switches and init[student[1] - 1 + i] == init[student[1] - 1 - i]:
                st = student[1] - i - 1
                ed = student[1] + i
            else:
                break
        for j in range(st, ed):
            init[j] = (init[j] + 1) % 2

for i in range(0, switches, 20):
    print(*init[i: i + 20])
