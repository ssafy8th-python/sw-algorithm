# 회의실 배정
# 최대 사용할 수 있는 회의 개수 출력
n = int(input())
lst = []
for _ in range(n):
    s, f = map(int, input().split())
    lst.append([f,s])
lst = sorted(lst)
k = 0
L = [k]
for i in range(1, n):            # 인덱스
    if lst[i][1] >= lst[k][0]:   # 시작 시간이 끝나는 시간보다 크거나 같다면
        L.append(i)
        k = i
print(len(L))
