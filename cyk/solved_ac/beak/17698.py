# 막대기
# N개의 막대기에 대한 높이 정보가 주어질 때 오른쪽에서 보아서 몇 개가 보이는지를 알아내는 프로그램을 작성하라
import sys
N = int(input())
ST = []
for _ in range(N):
    a = int(sys.stdin.readline())
    if not ST:
        ST.append(a)
    else:
        if a >= ST[-1]:
            while ST and a >= ST[-1]:
                ST.pop()
            ST.append(a)
        else:
            ST.append(a)
print(len(ST))