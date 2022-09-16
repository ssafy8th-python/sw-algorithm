# 세제곱근을 찾아라
'''
3
27
7777
64
'''
# 양의 정수 N에 대하여 N = x**3가 되는 양의 정수 x를 구하여라, N(1≤N≤10**18)
# 존재하지 않으면 -1을 출력
import math
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    print(f'#{tc}', end=" ")
    if math.isclose(math.ceil(n**(1/3)), n**(1/3)):
        print(math.ceil(n**(1/3)))
    else:
        print(-1)
