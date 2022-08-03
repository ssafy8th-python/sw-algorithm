# 10989 수 정렬하기 3
# 주소: https://www.acmicpc.net/problem/10989

# 제출한 답
N = int(input())

num_lst = []
for i in range(N):    # N만큼 반복하면서 n을 리스트에 넣음
    n = int(input())
    num_lst.append(n)

num_lst.sort()    # 리스트 정렬

for j in range(N):    # N만큼 반복하면서 리스트 차례로 프린트
    print(num_lst[j])


# 다른 답
