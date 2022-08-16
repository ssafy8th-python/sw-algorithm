# 설탕 봉지 3kg과 5k이 있을 때 Nkg을 가져가기 위해 가져가야하는 가장 적은 봉지 수 구하기

n = int(input())

three = n // 3 # 3봉지 가져갈 때의 한계 값
five = n // 5 # 5봉지 가져갈 때의 한계 값
result = []

for x in range(three+1): # 한계값까지의 수 넣어서 만족하면 result에 추가
    for y in range(five+1):
        if 3 * x + 5*y == n:
            result.append(x+y)

if result: # result에 값이 있으면 가장 적은 경우의 수 출력
    print(min(result))
else:# 없다면 -1
    print(-1)

