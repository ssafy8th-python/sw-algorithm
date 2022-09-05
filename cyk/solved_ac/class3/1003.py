# 피보나치 함수에서 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성
#
# def fibo(n):
#     global cnt_0
#     global cnt_1
#     if n == 0:
#         cnt_0 += 1
#         return 0
#     elif n == 1:
#         cnt_1 += 1
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)

def fibo(n):
    f = [0,1]
    for i in range(2, n+1):
        f.append(f[i-1]+f[i-2])
    return f
N = int(input())
for _ in range(N):
    num = int(input())
    if num == 0:
        print(1,0)
    else:
        print(fibo(num))
        print(fibo(num)[-2],fibo(num)[-1])