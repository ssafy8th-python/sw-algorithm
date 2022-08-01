# 1989 초심자의 회문검사
# 주소: https://url.kr/pebyaw

# [문제]
# "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
# 단어를 입력 받아 회문이면 1을 출력하고, 아니라면 0을 출력하는 프로그램을 작성하라.


# [제약 사항]
# 각 단어의 길이는 3 이상 10 이하이다.


# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 하나의 단어가 주어진다.


# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


# [제출한 답]
# a = int(input())

# for i in range(1, a+1):
#     b = input()
#     c = ''

#     for d in b:
#         c = d + c

#     if b == c:
#         print(f'#{i} 1')
#     else:
#         print(f'#{i} 0')


# [다른 답]
# T = int(input())
 
# for test_case in range(1, T + 1):   # #n 을 위한 함수
     
#     text = input()  # 글자적는 칸
#     text_len = len(text)    #글자 수

#     for i in range(text_len//2):            # 가운데 기준으로 절반이 서로 같으면 회문임
#         if text[i] != text[text_len-1-i]:   # text[i]: 글자 앞부터 i번째까지 글자
#             result = 0                      # text[text_len-1-i]: 마지막 글자는 글자 길이에서 1을 뺀 곳임
#                                             # 거기서 하나씩 빼면서 글자 출력
#             break                           # if 만족하면 break하고 result에 0 넣음
#     else:
#         result = 1                          # if 만족 못하고 for끝까지 수행하면 result에 1 넣음
         
#     print(f'#{test_case} {result}')