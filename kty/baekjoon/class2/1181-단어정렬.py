N = int(input())
words = list(set([input() for _ in range(N)]))
words.sort()
words.sort(key=len)
for i in words:
    print(i)