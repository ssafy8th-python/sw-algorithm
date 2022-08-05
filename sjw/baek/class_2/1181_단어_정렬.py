# 1181 단어 정렬
# 주소: https://www.acmicpc.net/problem/1181

# 제출한 답
# N = int(input())

# word_dict = {}              # 글자 길이 별로 묶어서 정렬
#                             # 거기 내에서 다시 사전순으로 정렬3
# for _ in range(N):
#     word = input()
#     if word_dict.get(len(word)) == None:
#         word_dict[len(word)] = [word]
#     elif word in word_dict.get(len(word)):
#         continue
#     elif len(word) in word_dict:
#         word_dict[len(word)].append(word)

# word_lst = sorted(list(word_dict.items()))

# for i in word_lst:
#     i[1].sort()
#     for j in i[1]:
#         print(j)


# 다른 답
# from sys import stdin

# def func():
#     n = int(stdin.readline())       # 숫자 입력하는 것

#     ls = set()                      # 셋으로 중복값 제거
#     for word in stdin:              # 인풋주는 것
#         ls.add(word.rstrip())       # stdin으로 받으면 오른쪽에 이상한거 지우는 것

#     ls = list(ls)                   # set을 list로 교체
#     ls.sort()                       # 사전순으로 정렬
#     ls.sort(key=lambda x: len(x))   

#     print('\n'.join(ls))

# if __name__ == '__main__':
#     func()