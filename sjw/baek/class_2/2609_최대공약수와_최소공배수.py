# 2609 최대공약수와 최소공배수
# 주소: https://www.acmicpc.net/problem/2609

# 제출한 답
# n, m = map(int, input().split())

# n_set = set() 
# for i in range(1, n + 1):
#     if n % i == 0:
#         n_set.add(i)

# m_set = set() 
# for j in range(1, m + 1):
#     if m % j == 0:
#         m_set.add(j)

# yak = max(n_set & m_set)
# bae = (n * m) / yak

# print(int(yak))
# print(int(bae))


# 다른 답
# def gcd(a,b):               # a: 큰 수 / b: 작은 수
#     if a%b == 0:            # a를 b로 딱 나눠떨어질 때까지 실행되는 재귀함수
#         return b
#     return gcd(b,a%b)       # 작았던 수를 큰 수로 나머지를 작은 수로

# num1,num2 = map(int,input().split())

# a = max(num1,num2)
# b = min(num1,num2)
# c = gcd(a,b)

# print(c)
# print(c*(a//c)*(b//c))      # 공약수 * a를 공약수로 나눈 답 * b를 공약수로 나눈 답