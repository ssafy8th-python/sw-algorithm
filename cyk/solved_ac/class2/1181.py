N = int(input())
dict_2 = dict()
for i in range(N):
    # ord_sum = 0
    word = input()
    
    if  not (len(word) in dict_2.keys()) :
        dict_2[len(word)] = [word]
    else :
        dict_2[len(word)].append(word)

# print(dict_2)
# {3: ['but'], 1: ['i'], 4: ['wont', 'more', 'more', 'wait'], 8: ['hesitate'], 2: ['no', 'no', 'it', 'im'], 6: ['cannot'], 5: ['yours']}
dic = dict(sorted(dict_2.items()))
# print(list(dic.values()))
for i in list(dic.values()):
    for j in sorted(list(set(i))) :
        print(j)