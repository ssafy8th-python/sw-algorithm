# 소수 구하기 M 이상 N 이하의 소수를 모두 출력하는 프로그램
max_lm = 1000**2
arr = [True] * (max_lm+1)

arr[0], arr[1] = False, False

for i in range(2, int(max_lm**0.5)):
    if arr[i]: #True 일때 => 소수 일 때
        mult = 2
        while i * mult <= max_lm: # 소수가 아닌 수 전부 제거(False)
            arr[i * mult] = False
            mult += 1


s, e = map(int, input().split())

for i in range(s,e+1):
    if arr[i]:
        print(i)