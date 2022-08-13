# 버블 정렬
# def BubbleSort(a, N):
#     for i in range(N-1, 0, -1): #첫번째 원소부터 인접한 원소끼리 계속 자리 교환하면서 맨 마지막자리까지 이동
#         for j in range(0,i):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
# n = 10
# for i in range(n-1, 0, -1):
#     for j in range(0,i):
#         print(j)


# def reverse(s):
#     new_s = ''
#     for i in range(len(s)):
#         new_s += s[len(s)-i-1]
#     return new_s
#
# def reverse_2(s):
#     s = list(s)
#     for i in range(len(s)//2):
#         s[i],  s[len(s)-i-1] = s[len(s)-i-1], s[i]
#     s =''.join(s)
#     return s
#
#
#
#
# s = 'sgnirts siht esreveR'
# print(reverse(s))
#
# print(reverse_2(s))

# s1 = 'abc'
# s2 = 'abc'
# s3 = 'def'
# s4 = s1
# s5 = s1[:2] + 'c'
# print(s1 == s2, s1 is s2)
# print(s1 == s3, s1 is s3)
# print(s1 == s4, s1 is s4)
# print(s1 == s5, s1 is s5)
#

# def strcmp(str1, str2):
#     if str1 == str2:
#         return 0
#     if str1 > str2:
#         return 1
#     else:
#         return -1
#
# print(strcmp('z', 'abc'))

# def myStr(value):
#     if value < 0:
#         result =''
#         value = value * -1
#         while value > 0:
#             result = chr(value % 10 + ord('0')) + result
#             value = value // 10
#         return '-' + result
#     else:
#         result = ''
#         while value > 0:
#             result = chr(value % 10 +ord('0')) + result
#             value = value // 10
#         return result


# def myStr(value):
#     s =''
#     isMinus = False
#     if value <0:
#         isMinus = True
#         value = value * -1
#
#     while value > 0:
#         s = chr(value % 10 +ord('0')) + s
#         value = value // 10
#     if isMinus:
#         s = '-' + s
#     return s
#
# print(myStr(123))
# print(myStr(-321))

# 찾으면 위치 패턴의 시작 위치를 return하고 못찾으면 -1을 return
def find(t, p):
    N = len(t)
    M = len(p)
    for i in range(N-M+1):
        if t[i:i+M] == p:
            return i
    else :
        return -1

t = 'a pattern matching algorithm test'
p = 'a pattern'
print(find(t,p))


