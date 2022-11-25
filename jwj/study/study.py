#
# # 카운트 정렬
# N = int(input())
#
# arr = list(map(int, input().split()))
#
# '''
# 9
# 7 4 2 0 0 6 0 7 0
# '''
#
# tmp = [0] * N
# c = [0] * 101        #0부터 100까지 숫자 개수
# for i in range(N):    # 카운트
#     c[arr[i]] += 1
#
# print(c)
#
# for j in range(1, 101):      # 개수 누적
#     c[j] += c[j-1]
#
# print(c)
#
# for i in range(N-1, -1, -1):    # 원본을 뒤에서부터 읽으면서 정렬 결과를 tmp에 저장(안전하게 정렬)
#     c[arr[i]] -= 1              # 몇 개인지 개수에서 인덱스로 변환
#     tmp[c[arr[i]]] = arr[i]
#
# print(tmp)
#
# # input
# N = int(input())
#
# arr = [list(map(int, input())) for _ in range(N)]



# # 모든 부분 집함에 접근하는 방법
#
# # 2의 6승 64  => 0 ~ 63
# # =====i====
# # 0 0 0 0 0 0
# # 0 0 0 0 0 1   3
# # 0 0 0 0 1 0   6
# # 0 0 0 0 1 1   3, 6
# # 위의 방식으로 모든 부분 집함에 접근
#
# # ====1 << j====
# # 0 0 0 0 0 0   index :0
# # 0 0 0 0 0 1   index : 1
# # 0 0 0 0 1 0   index : 2
# # 0 0 0 1 0 0
#
arr = [3, 6, 7, 1, 5, 4]

n = len(arr)

for i in range(1 << n):
    for j in range(n):
        if i & (1 << j):
            print(arr[j], end=', ')

    print()
print()

# print(1 << 0)

# string reverse
#
# def rev(s):
#     for idx in range(len(s)//2):
#         s[idx], s[len(s)-idx-1] = s[len(s)-idx-1], s[idx]
#
#
# s = "abcd"
# s = list(s)
#
# rev(s)
#
# s = ''.join(s)
#
# print(s)
#
#
# def my_strcmp(str1, str2) :
#     i = 0
#     while (str1[i] != '\0'):
#         if (str1 != str2[i]):
#             break
#         i += 1
#
#     return (ord(str1[i]) - ord(str2[i]))
#

# ==============itoa 함수 구현==============
#
# print(my_strcmp('abcd', 'b'))
# print(my_strcmp( 'b', 'abcd'))
# print(my_strcmp('abcd', 'abcd'))
#
# def itoa(number):
#     minus = False
#     if number < 0:
#         minus = True
#
#     if minus:
#         number *= -1
#
#     i = []
#     while number != 0:
#         i.append(number%10)
#         number //= 10
#
#     res = ''
#     for idx in range(len(i)-1, -1, -1):
#         res +=  chr(i[idx] + ord('0'))
#
#     if minus:
#         res = '-' + res
#
#     return res
#
# print(itoa(123))
# print(itoa(3214))
# print(itoa(-321))

# ================찾으면 패턴의 시작위치를 return 못찾으면 -1을 return 하는 함수================

#
# def find(t, p):
#     i = j = 0
#
#     while i < N and j < M:
#         if t[i] != p[j]:
#             i = i - j + 1
#             j = 0
#         else:
#             i += 1
#             j += 1
#
#     if j == M:
#         return i - M
#     else:
#         return -1
#
#
# t = 'a patern matching algorithm test'
# p = 'rithm'
# N = len(t)
# M = len(p)
#
# print(find(t, p))
#
