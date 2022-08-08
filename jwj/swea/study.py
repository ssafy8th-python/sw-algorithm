
# 카운트 정렬
N = int(input())

arr = list(map(int, input().split()))

'''
9
7 4 2 0 0 6 0 7 0
'''

tmp = [0] * N
c = [0] * 101        #0부터 100까지 숫자 개수
for i in range(N):    # 카운트
    c[arr[i]] += 1

print(c)

for j in range(1, 101):      # 개수 누적
    c[j] += c[j-1]

print(c)

for i in range(N-1, -1, -1):    # 원본을 뒤에서부터 읽으면서 정렬 결과를 tmp에 저장(안전하게 정렬)
    c[arr[i]] -= 1              # 몇 개인지 개수에서 인덱스로 변환
    tmp[c[arr[i]]] = arr[i]

print(tmp)
