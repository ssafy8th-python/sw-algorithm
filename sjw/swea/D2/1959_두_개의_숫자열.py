# 1959. 두 개의 숫자열
# 주소: https://url.kr/bx64md

# [문제]
# N 개의 숫자로 구성된 숫자열 Ai (i=1~N) 와 M 개의 숫자로 구성된 숫자열 Bj (j=1~M) 가 있다.
# 아래는 N =3 인 Ai 와 M = 5 인 Bj 의 예이다.

# Ai 나 Bj 를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있다.
# 단, 더 긴 쪽의 양끝을 벗어나서는 안 된다.
 
# 서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.
# 위 예제의 정답은 아래와 같이 30 이 된다.
 

# [제약 사항]
# N 과 M은 3 이상 20 이하이다.


# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
# 두 번째 줄에는 Ai,
# 세 번째 줄에는 Bj 가 주어진다.


# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


# [제출한 답1]

# T = int(input())
#
# for i in range(1, T + 1):
#
#     N, M = map(int, input().split())
#     Ai = list(map(int, input().split()))
#     Bj = list(map(int, input().split()))
#
#     if M >= N:
#         a = M - N
#         b = 0
#         d = []
#
#         for j in range(0, a + 1):
#             for k in range(0, N):
#                 c = int(Ai[k]) * (Bj[k + j])
#                 b += c
#             d.append(b)
#             b = 0
#         print(f'#{i} {max(d)}')
#
#     else:
#         a = N - M
#         b = 0
#         d = []
#
#         for j in range(0, a + 1):
#             for k in range(0, M):
#                 c = int(Bj[k]) * (Ai[k + j])
#                 b += c
#             d.append(b)
#             b = 0
#         print(f'#{i} {max(d)}')


# [제출한 답2]
# T = int(input())                              # 테스트 케이스 인풋

# for i in range(1, T + 1):                     # T만큼 반복

#     N, M = map(int,input().split())           # N, M 인풋
#     Ai = list(map(int, input().split()))      # Ai 인풋
#     Bj = list(map(int, input().split()))      # Bj 인풋

#     if M < N :                                # 큰 수(M)에서 작은 수(N)를 빼야하기 때문에
#         M, N = N, M                           # N이 더 크면 둘을 교환
#         Ai, Bj = Bj, Ai

#     a = M - N                                 # 위치를 변경하는 횟수
#     b = 0                                     # 마주 보는 것을 곱한 값을 더해줄 변수
#     d = []                                    # 구한 값을 추가해줄 빈 리스트
    
#     for j in range(0, a + 1):                 # 위치를 변경하는 횟수(a) + 위치 변경 전(1)
#         for k in range(0, N):                 # N은 처음부터 끝까지 다 써야하기때문에 N만큼 반복
#             c = int(Ai[k]) * (Bj[k + j])      # 각 자리수 곱하기
#             b += c                            # 곱한 값을 더하기
#         d.append(b)                           # 더한 값을 리스트에 추가
#         b = 0                                 # b를 0으로 초기화
#     print(f'#{i} {max(d)}')                   # 리스트 중 가장 큰 값을 출력


# [다른 답1]
# T = int(input())
 
# for test_case in range(T):
#     N, M = map(int, input().split())
     
 
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
 
#     result = 0
 
#     if N > M:
#         N, M = M, N
#         A, B = B, A
 
#     for i in range(M-N+1):
#         tmp = 0
#         for j in range(N):
#             tmp += A[j] * B[j+i]
 
#         if tmp > result:
#             result = tmp
 
#     print(f'#{test_case+1} {result}')


# # [다른 답2]
# for i in range(int(input())):           # 테스트 케이스 인풋 / T만큼 반복
#     cnt=0                               # cnt = 0
#     a,b=list(map(int,input().split()))  # N, M 인풋
#     l=list(map(int,input().split()))    # Ai 인풋
#     k=list(map(int,input().split()))    # Bj 인풋
#     if a>b:                             # 큰 수(b)에서 작은 수(a)를 빼야하기 때문에
#         a,b=b,a                         # N이 더 커지면 N과 M, Ai와 Bj를 바꿈
#         l,k=k,l
#     o=0                                 # o = 0
#     for j in range(b-a+1):              # M과 N의 차이만큼 반복
#         p=0                             # p = 0
#         for t in range(a):              # 작은 수만큼 반복
#             p+=l[t]*k[t+j]              # p에 (작은 수의 각각의 요소 * 큰 수의 요소(한 칸씩 땡김))한 값을 더함
#         if o<p:                         # p와 o를 비교해서 p가 더 크면 o에 값을 대입
#             o=p                         # 가장 큰 수만 남기는 과정
#     print(f'#{i+1} {o}')                # o를 프린트