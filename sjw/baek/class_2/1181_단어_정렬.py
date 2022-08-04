# 1181 단어 정렬
# 주소: https://www.acmicpc.net/problem/1181

# 제출한 답
N = int(input())

word_dict = {}

for _ in range(N):
    word = input()
    if word in word_dict.get(len(word)):
        continue
    if len(word) in word_dict:
        word_dict[len(word)].append(word)
    else:
        word_dict[len(word)] = [word]
print(word_dict)
word_lst = sorted(list(word_dict.items()))

for i in word_lst:
    i[1].sort()
    for j in i[1]:
        print(j)


# 글자 길이 별로 묶어서 정렬
# 거기 내에서 다시 사전순으로 정렬3