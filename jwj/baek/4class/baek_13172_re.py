
MOD = 1000000007


def divisionPow(num, exp):
    if exp == 1:
        return num

    half = divisionPow(num, exp//2)

    if exp % 2:
        return half * half * num % MOD
    else:
        return half * half % MOD


M = int(input())

result = 0

for _ in range(M):
    N, S = map(int, input().split())

    # 기댓값을 구함
    # 페르마의 소정리 A * B^(MOD-2) % MOD => S * N^(MOD-2) % MOD
    result += S * divisionPow(N, MOD-2) % MOD

    # 기댓값 더하기기
    reult %= MOD

print(result)
