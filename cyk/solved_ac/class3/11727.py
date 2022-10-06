# 2xn 타일링
# 2xn 직사각형을 1x2, 2x1, 2x2 타일로 채우는 방법의 수
# 점화식 : f(n-1) + 2*f(n-2)

lst = [0]*1001
lst[1] = 1
lst[2] = 3
for i in range(3, 1001):
    lst[i] = lst[i-1] + 2*lst[i-2]

n = int(input())
print(lst[n]%10007)