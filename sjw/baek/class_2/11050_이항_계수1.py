# 11050 이항 계수 1
# 주소: https://www.acmicpc.net/problem/11050

# 제출한 답
def facto(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * facto(n-1)

N, K = map(int, input().split())            # 이항 계수 공식 그대로 만듦

if K < 0 or K > N:
    print(0)
else:
    result = facto(N) / (facto(K)*facto(N-K))

    print(int(result))