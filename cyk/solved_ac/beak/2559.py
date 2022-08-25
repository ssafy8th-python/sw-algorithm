# 수열
# 투 포인터: start, end 두 개의 포인터 사용, start <= end
# 슬라이딩 윈도우: 교집합의 정보를 공유하고 차이가 나는 양쪽 끝 원소만 갱신하는 방법
# 투 포인트는 구간의 넓이가 조건에 따라 유동적으로 변하며 슬라이딩 윈도우 알고리즘은 항상 구간의 넓이가 고정되어 있음
'''
10 5
3 -2 -4 -9 0 3 7 13 8 -3
'''
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
s = list(map(int, input().split()))
sumS = sum(s[0:K])    # 처음 구간의 합 => -12
mx = sumS
for i in range(0, N-K):
    sumS = sumS - s[i] + s[i+K]
    if mx < sumS:
        mx = sumS
print(mx)
