# 2920 음계
# 주소: https://www.acmicpc.net/problem/2920

# 제출한 답
# ascending = list(range(1, 9))
# descending = list(range(8, 0, -1))

# num = list(map(int, input().split()))

# if num == ascending:
#     print('ascending')
# elif num == descending:
#     print('descending')
# else:
#     print('mixed')
 

# 다른 답
# A = list(map(int, input().split()))

# if A == sorted(A):                    # 오름차순과 내림차순을 미리 적어놓을 필요없이
#     print('ascending')                # sorted를 쓰면 된다.
# elif A == sorted(A, reverse=True):
#     print('descending')
# else:
#     print('mixed')