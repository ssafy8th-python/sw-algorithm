# 1157 단어 공부
# 주소: https://www.acmicpc.net/problem/1157

# 제출한 답
# word = input()
# word = word.upper()

# word_dict = {}

# for i in word:
#     if i in word_dict:
#         word_dict[i] += 1
#     else:
#         word_dict[i] = 1

# word_sort = sorted(word_dict.items(), key = lambda x : x[1], reverse = True)

# if len(word_sort) > 1 and word_sort[0][1] == word_sort[1][1]:
#     print('?')
# else:
#     print(word_sort[0][0])

# 다른 답
# st = input().lower()
# dic ={}
# for chr in st:
#     if chr in dic:
#         dic[chr] += 1
#     else:
#         dic[chr] = 1
# listt = [k for k,v in dic.items() if max(dic.values()) == v]  # 리스트 컴프리헨션을 사용하면 모든 맥스값들을 모아준다.

# if len(listt) > 1:
#     print('?')
# else:
#     k=(max(dic, key=dic.get))
#     print(k.upper())