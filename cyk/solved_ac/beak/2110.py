# 공유기 설치
# 다시풀기
'''
5 3
1
2
8
4
9
'''
import sys
input = sys.stdin.readline
lst = []
N, C = map(int, input().split())
for _ in range(N):
    lst.append(int(input()))
lst = sorted(lst)
start = 1
end = lst[-1] - lst[0]
answer = 0
while start <= end:
    middle = (start + end) // 2     # 공유기 설치 최대 간격
    num = 1     # 첫번째 집에 공유기 설치
    cur = lst[0]
    for i in range(1, len(lst)):
        if lst[i] >= cur + middle:
            num += 1
            cur = lst[i]

    if num >= C:    #공유기 설치 대수가 공유기 개수보다 크면
        start = middle + 1
        answer = middle
    else:
        end = middle - 1
print(answer)